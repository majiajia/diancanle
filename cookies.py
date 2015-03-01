#! /usr/bin/env python
import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define,options
define("port",default=8000,help="run on the given port",type=int)

class BaseHandle(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user_name")

class IndexHandle(BaseHandle):
    def get(self):



class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/",IndexHandle)
        ]
        settings = dict(
            static_path=os.path.join(os.path.dirname(__file__),"static"),
            template_path=os.path.join(os.path.dirname(__file__),"template")
        )
        tornado.web.Application.__init__(self,handlers,**settings)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()