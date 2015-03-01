#! /usr/bin/env python
import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define,options
define("port",default=8000,help="running on the gienv port",type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        # self.render("index.html")
        items = ["apple","dell"]
        title = "this is a list test page"
        self.render("list.html",title=title,items=items)



class PoemMakerHandler(tornado.web.RequestHandler):
    def post(self):
        noun1 = self.get_argument("noun1")
        noun2 = self.get_argument("noun2")
        verb = self.get_argument("verb")
        self.render("poem.html",noun1=noun1,noun2=noun2,verb=verb)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r"/",IndexHandler),
            (r"/poem",PoemMakerHandler)
        ],
        static_path=os.path.join(os.path.dirname(__file__),"static"),
        template_path=os.path.join(os.path.dirname(__file__),"template")
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()