#! /usr/bin/env python
import os.path

import tornado.httpserver
import tornado.web
import tornado.ioloop
import tornado.options

from tornado.options import define,options
define("port",default=8000,help="running on the given port",type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", header_text="header_text nwe", footer_text="footer_text new", page_title="page_title new")


class HelloModule(tornado.web.UIModule):
    def render(self):
        return "this is produced by hello module"


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/",IndexHandler)
        ]
        settings = dict(
            static_path=os.path.join(os.path.dirname(__file__),"static"),
            template_path=os.path.join(os.path.dirname(__file__),"template"),
            ui_modules={"Hello":HelloModule}
        )
        tornado.web.Application.__init__(self,handlers,**settings)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()



