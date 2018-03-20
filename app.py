import os
from http.server import HTTPServer

from flask import Flask
from nikola.plugins.command.serve import OurHTTPRequestHandler


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
        httpd = HTTPServer((kwargs['address'], port),
                           OurHTTPRequestHandler)
        sa = httpd.socket.getsockname()
        print("Serving HTTP on", sa[0], "port", sa[1], "...")
        httpd.serve_forever()


if __name__ == "__main__":
    execute(address="127.0.0.1")
