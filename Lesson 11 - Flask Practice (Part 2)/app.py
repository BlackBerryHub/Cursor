import hashlib
import os
import uuid

import catday
import utils
from flask import Flask, Response, abort, send_file, render_template, request
from PIL import Image, ImageFile
import io
import logging
import random

from time import perf_counter

# set maximum block size to 10 megabytes
ImageFile.LOAD_TRUNCATED_IMAGES = True
ImageFile.MAX_BLOCK_SIZE = 10485760

app = Flask(__name__)


# Note:
#   If a rule ends with a slash and is requested without a slash by the user,
#   the user is automatically redirected to the same page with a trailing 
#   slash attached.
#   If a rule does not end with a trailing slash and the user requests
#   the page with a trailing slash, a 404 not found is raised.
# So we try to always define rules with trailing slashes '/'

@app.route('/', methods=["GET", "POST"])
def customtext():
    first_name = ''
    if request.method == "POST":
        first_name = request.form.get("fname")
        num = request.form.get("num")
        src = f"catoftheday?num={num}&fname={first_name}"
        cat_of_the_day = f'<img id="cat-image" src="{src}" alt="cat of the day">'

    gallery_html = ''
    for image in range(len(catday.CATS)):
        gallery_html += f'<button class="img-choose" type="submit" form="form1" name="num" value="{image}"'\
                        f'method="POST"><img src="/cats/cat{image}.png" alt="cat"></button>'

    if request.method == "GET":
        cat_of_the_day = f'<img id="cat-image" src="/catoftheday.jpg" alt="cat of the day">'

    return render_template("catoftheday.html", gallery=gallery_html, cat_of_the_day=cat_of_the_day)


def get_cat(numext, try_random=False):
    try:
        ret = catday.find_cat_file(numext=numext,
                                   try_random=try_random)
    except ValueError:      # integer unconvertable or wrong range
        abort(404, 'Wrong image number')
    else:
        app.logger.debug('Retrieve image "%s" for base %s with ext "%s"', *ret)
        return ret


@app.route('/cats/cat<int:num>.<string:ext>')
def cat_original(num, ext):
    t_start = perf_counter()    # measure request time

    file, base, ext = get_cat(f'{num}.{ext}', try_random=False)

    name = f'cat{base}{ext}'   # the filename passed to browser
    
    app.logger.debug('Original extension is %s', file.suffix)
    
    # if the extension is different, perform conversion with PIL
    if ext.lower() != file.suffix.lower():
        
        try:
            img = Image.open(file)
            # Save to buffer in memory and serve with Flask
            buf = utils.ImageIO(img, ext=ext)
        except utils.ImageIOError as err:
            abort(400, str(err))
        else:
            # now our file gets mocked by conversion result
            file = buf
    
    # if the file has the same extension,
    # don't convert at all and return directly

    took = perf_counter() - t_start

    if app.logger.isEnabledFor(logging.DEBUG):
        msg = f'Request took {took * 1000:.2f} ms'
        app.logger.debug(msg)

    return send_file(file, as_attachment=False, download_name=name)

def process_image(file, text, ext):
    try:
        img = Image.open(file)
        bgcolor = (255, 255, 255, int(255 * 0.4))
        cut = catday.cutter.text_cutout(img, text, bgcolor=bgcolor)
        if ext in ['.jpg', '.jpeg', '.jfif']:
            # eliminate alpha-channel as JPEG has no alpha
            cut = cut.convert('RGB')
        file = utils.ImageIO(cut, ext=ext)
    except utils.ImageIOError as err:
        abort(400, str(err))
    return file

@app.route('/catoftheday', methods=["GET"])
def cat_text():
    if request.method == "GET":
        first_name = request.args.get("fname")
        num = request.args.get("num")

        file, base, ext = get_cat(f"{num}.png", try_random=True)
        date = utils.DateTriple()  # try UADateTriple() here
        date_suffix = date.tostr(fmt='{day}_{month:.3}').lower()

        if not first_name:
            text = date.tostr(fmt='{weekday:.3},\n{day}\n{month:.3}')
        else:
            text = first_name

        file = process_image(file, text, ext)

        return send_file(file, as_attachment=False, download_name=first_name)


@app.route('/catoftheday<name>')
def cat_date(name):

    file, base, ext = get_cat(name, try_random=True)

    date = utils.DateTriple()       # try UADateTriple() here
    date_suffix = date.tostr(fmt='{day}_{month:.3}').lower()
    text = date.tostr(fmt='{weekday:.3},\n{day}\n{month:.3}')
    file = process_image(file, text, ext)

    # passed to browser
    name = f'catoftheday{base}-{date_suffix}{ext}'
    return send_file(file, as_attachment=False, download_name=name)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        hashsum = hashlib.md5(file.read()).hexdigest()

        # check for decompression bomb before saving file
        try:
            with Image.open(file.stream) as img:
                pass
        except:
            return 'File is a decompression bomb!'

        if not catday.check_duplicate(hashsum):
            filename = str(uuid.uuid4()) + '.jpg'  # Set a unique filename
            file.stream.seek(0)
            file.save(os.path.join(app.root_path, 'static/uploaded/') + filename)
            return 'File uploaded successfully!'
        else:
            return 'File already exists!'


if __name__ == '__main__':
    import logging
    app.logger.setLevel(logging.DEBUG)
    app.run(host='127.0.0.1', port=5000, debug=True)