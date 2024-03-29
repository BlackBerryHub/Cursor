from functools import lru_cache
from flask import Flask, abort, request, Response

from statapi import methods

app = Flask(__name__)


@app.route('/stats/')
@lru_cache(maxsize=1)  # can use cuz no flask proxies refered
def stats_root():
    ret = """
        <b>Available endpoints:</b>
        /stats/ - list of all methods
        /stats/&lt;method_name&gt;/ - get stats for a specific method
        """.replace('\n', '<p>')
    methods_list = "<li>".join(methods)
    ret += f"<b>Available methods:</b><li>{methods_list}"
    return ret  # auto-converted to json by flask


@app.route('/stats/<string:method>')
def stats(method):
    method_args = request.args.to_dict()
    print(method_args)

    try:
        func = methods[method]
    except KeyError:
        abort(404, f'Method {method} not found')

    format_arg = method_args.get('format', None)

    try:
        res, mime = func(format_arg, method_args)
    except Exception as exc:
        if format_arg is not None:
            abort(400, f"The requested format '{format_arg}' is not supported for this method.")
        else:
            abort(400, "An error occurred while processing the request.")

    return Response(res, mimetype=mime)


if __name__ == '__main__':
    # We need to set logging to be able to see everything
    import logging
    app.logger.setLevel(logging.DEBUG)

    # (!) Never run your app on '0.0.0.0 unless you're deploying
    #     to production, in which case a proper WSGI application
    #     server and a reverse-proxy is needed
    #     0.0.0.0 means "run on all interfaces" -- insecure
    app.run(host='127.0.0.1', port=5000, debug=True)
