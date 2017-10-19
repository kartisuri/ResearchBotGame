#!/usr/bin/env python3
import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop
import json
import os
import signal
import tornado.options

from os.path import abspath, dirname, join

is_closing = False


class IndexPageHandler(tornado.web.RequestHandler):

    def data_received(self, chunk):
        pass

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers",
                        "Access-Control-Allow-Headers,Origin,Accept, X-Requested-With, " +
                        "Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, HEAD')
        self.set_header("Access-Control-Allow-Credentials", "false")
    
    def post(self):
        if self.request.body:
            print("Got JSON data: ", self.request.body)
            data = json.loads(self.request.body)
            if data['round'] == '0':
                log_chat(data['session'], data['id'], data['text'])
            else:
                log_round_proposals(data['session'], data['round'], data['proposals'])

    def get(self):
        pass

    def options(self, *args, **kwargs):
        pass


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [(r'/', IndexPageHandler)]
        settings = {'template_path': 'templates'}
        tornado.web.Application.__init__(self, handlers, **settings)


def log_chat(session, id_value, text):
    file_name = join(dirname(abspath(__file__)), 'Chat_Logs_' + session + '.txt')
    if not os.path.isfile(file_name):
        with open(file_name, 'w') as ro:
            string = id_value + '\t' + text + '\n'
            ro.write(string)
    else:
        with open(file_name, 'a') as ro:
            string = id_value + '\t' + text + '\n'
            ro.write(string)


def log_round_proposals(session, round_num, proposals):
    file_name = join(dirname(abspath(__file__)), 'Round_Proposals_' + session + '.txt')
    if not os.path.isfile(file_name):
        with open(file_name, 'w') as ro:
            string = 'Round' + round_num + ' Proposals:\t' + str(proposals) + '\n'
            ro.write(string)
    else:
        with open(file_name, 'a') as ro:
            string = 'Round' + round_num + ' Proposals:\t' + str(proposals) + '\n'
            ro.write(string)


def signal_handler(signum, frame):
    print(signum, frame)
    global is_closing
    is_closing = True


def try_exit(): 
    global is_closing
    if is_closing:
        tornado.ioloop.IOLoop.instance().stop()


def test():
    log_round_proposals('ABC', '1', ['1', '2'])
    log_round_proposals('ABC', '2', ['c', 'd'])
    log_chat('ABC', 'P1', 'Hi')
    log_chat('ABC', 'B1', 'Hi there')
    log_round_proposals('DEF', '1', ['1', '2'])
    log_round_proposals('DEF', '2', ['c', 'd'])
    log_chat('DEF', 'P1', 'Hi')
    log_chat('DEF', 'B1', 'Hi there')

# test()	


if __name__ == '__main__':
    tornado.options.parse_command_line()
    signal.signal(signal.SIGINT, signal_handler)
    port = 5000
    ws_app = Application()
    server = tornado.httpserver.HTTPServer(ws_app)
    server.listen(port)
    tornado.ioloop.PeriodicCallback(try_exit, 100).start() 
    print("Game Log Server started on " + str(port))
    tornado.ioloop.IOLoop.instance().start()
