#! /usr/bin/env python
import os.path

import tornado.httpserver
import tornado.options
import tornado.ioloop
import tornado.web

from tornado.options import define,options
define("port",default=8000,help="running on the given port",type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html",page_title="page title new",header_text="header_text new",footer_text="footer_text new",body_text="body_text new")


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler)
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "template"),
            static_path=os.path.join(os.path.dirname(__file__), "static")
        )
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

    tornado.escape.linkify