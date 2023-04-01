from datetime import datetime, timedelta, timezone
import re
from flask import Flask, abort

app = Flask(__name__)

@app.route("/")
def date_time_info():
    return """Welcome, stranger!"""

@app.route("/datetime/")
@app.route("/datetime/<time_zone>")
def date_time(time_zone=None):
    if not time_zone:
        return f"Provided GMT parameter: {time_zone} <p> " \
               f"Time: {datetime.now()}"

    if re.match("^0|[+](?:1[0-2]|[0-9])$", time_zone):
        return f"Provided parameter: {time_zone} <p> " \
               f"Time: {datetime.now(tz=timezone(timedelta(hours=int(time_zone))))}"
    else:
        abort(406)


if __name__ == '__main__':
    app.run(debug=True, port=5000)