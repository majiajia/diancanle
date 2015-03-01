#! /usr/bin/env python
import textwrap
import os

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define,options
define("port", default=8000, help="running on the given port", type=int)


class ReverseHandler(tornado.web.RequestHandler):
    # http://localhost:8000/?greeting=lucy
    def get(self):
        a = self.get_argument("a")
        b = self.get_argument("b")
        self.write(a + "," + b)


class WrapHandler(tornado.web.RequestHandler):
    def post(self):
        text = self.get_argument("text")
        width = self.get_argument("width", 40)
        self.write(textwrap.fill(text, int(width)))
    def write_error(self, status_code, **kwargs):
        self.write("statue code : %d " % status_code)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers= [
            (r"/reverse/", ReverseHandler),
            (r"/wrap",WrapHandler)
        ],
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        template_path=os.path.join(os.path.dirname(__file__), "template")
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()