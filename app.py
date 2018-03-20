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
            if not os.path.isdir(out_dir):
                print("Error: Missing '{0}' folder?".format(out_dir))
            else:
                os.chdir(out_dir)
                httpd = HTTPServer((options['address'], options['port']),
                                   OurHTTPRequestHandler)
                sa = httpd.socket.getsockname()
                print("Serving HTTP on", sa[0], "port", sa[1], "...")
                httpd.serve_forever()

        execute(address=host, port=port)
        # super().run(host,port,debug, **options)


app = FlaskNew(__name__)
# @app.route('/')
# def index():
#     # from nikola import __main__
#     # import nikola
#     # import nikola.plugins.command
#     # import nikola.plugins.command.init
#     # import nikola.plugins.command.serve
#     # from nikola.plugin_categories import Command
#
#
#
#     return 'oks!'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
