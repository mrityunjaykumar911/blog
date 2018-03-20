import os
from http.server import HTTPServer

from flask import Flask
from nikola.plugins.command.serve import OurHTTPRequestHandler


class FlaskNew(Flask):
    def __init__(self, import_name):
        super().__init__(import_name)

    def run(self, host=None, port=None, debug=None, **options):
        def execute(**options):
            """Start test server."""
            out_dir = 'output'
            if os.path.exists(out_dir) is False:
                os.system('nikola build')
            if not os.path.isdir(out_dir):
                print("MJAY:\t Error: Missing '{0}' folder?".format(out_dir))
            else:
                os.chdir(out_dir)
                port = options['port']
                if port is None:
                    port = 8000
                httpd = HTTPServer((options['address'], port),
                                   OurHTTPRequestHandler)
                sa = httpd.socket.getsockname()
                print("Serving HTTP on", sa[0], "port", sa[1], "...")
                httpd.serve_forever()

        execute(address=host, port=port)
        # super().run(host,port,debug, **options)


app = FlaskNew(__name__)


if __name__ == "__main__":
    app.run(host="127.0.0.1")
