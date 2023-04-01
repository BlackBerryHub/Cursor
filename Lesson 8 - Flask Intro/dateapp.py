import inspect
import logging
from datetime import datetime, timedelta, timezone
import re
from flask import Flask, abort

app = Flask(__name__)

logging.basicConfig(filename="logs.log", level=logging.INFO)

@app.route("/")
def index():
    return date_time_info.__doc__

@app.route("/datetime")
def date_time_info():
    """
    Route /datetime, returns documentation and an example of how to use the method
    """
    return date_time.__doc__.replace('\n', '<p>')  # for replace I got the idea from BoyovEvgen

@app.route("/datetime/")
@app.route("/datetime/<time_zone>")
def date_time(time_zone=None):
    """
    Route /datetime/ returns the current date and time with the server time zone
    Route /datetime/+2 returns the date and time of the server in GMT+2
    Route /datetime/0 returns the date and time in Greenwich Mean Time
    """
    app.logger.info(f"Provided parameter: {time_zone}")
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