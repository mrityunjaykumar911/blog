import os
from http.server import HTTPServer

from flask import Flask, render_template
from nikola.plugins.command.serve import OurHTTPRequestHandler


class FlaskNew(Flask):
    def run(self, host=None, port=None, debug=None, **options):
        # super().run(host,port,debug,**options)
        print("MJAY: ",host,port)
        execute(address=host, port=port)


app = FlaskNew(__name__)


def execute(**kwargs):
    """Start test server."""
    out_dir = 'output'
    # if os.path.exists(out_dir) is False:
    #     os.system('nikola build')
    if not os.path.isdir(out_dir):
        print("MJAY:\t Error: Missing '{0}' folder?".format(out_dir))
    else:
        os.chdir(out_dir)
        port = kwargs.get('port', 8000)
        if port is None:
            port = 8000
        httpd = HTTPServer((kwargs['address'], port),
                           OurHTTPRequestHandler)
        sa = httpd.socket.getsockname()
        print("Serving HTTP on", sa[0], "port", sa[1], "...")
        httpd.serve_forever()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
