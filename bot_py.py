#!/usr/bin/env python3

import os
import sys
import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop
import json
import signal
import tornado.options

from os.path import abspath, dirname, join

is_closing = False

class IndexPageHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("Welcome to the Game Logging Server")
    
    def post(self):
        data = {'round': -1}
        if self.request.body:
            print("Got JSON data: ", self.request.body)
            data = json.loads(self.request.body)
            if data['round'] == 0:
                log_chat(data['session'], data['id'], data['text'])
            elif data['round'] in range(1,11):
                log_round_proposals(data['session'], data['round'], data['proposals'])		
            else:
                print("Round number not specified")
            self.finish()

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [(r'/', IndexPageHandler)]
        settings = {'template_path': 'templates'}
        tornado.web.Application.__init__(self, handlers, **settings)
		
def log_chat(session, id, text):
    file_name = join(dirname(abspath(__file__)), session + '_chat.txt')
    if not os.path.exists(file_name):
        with open(file_name, 'w') as chat:
            string = id + ':\t' + text
            chat.write(string)
    else:
        with open(file_name, 'a') as chat:
            string = id + ':\t' + chat
            chat.write(string)
        
def log_round_proposals(session, round, proposals):
    file_name = join(dirname(abspath(__file__)), session + '_proposals.txt')
    if not os.path.exists(file_name):
        with open(file_name, 'w') as ro:
            string = 'Round ' + round + ':\t' + proposals + '\n'
            ro.write(string)
    else:
        with open(file_name, 'a') as ro:
            string = 'Round ' + round + ':\t' + proposals + '\n'
            ro.write(string)

def signal_handler(signum, frame):
    global is_closing
    is_closing = True

def try_exit(): 
    global is_closing
    if is_closing:
        tornado.ioloop.IOLoop.instance().stop()

if __name__ == '__main__':
    tornado.options.parse_command_line()
    signal.signal(signal.SIGINT, signal_handler)
    port = 6000
    ws_app = Application()
    server = tornado.httpserver.HTTPServer(ws_app)
    server.listen(port)
    tornado.ioloop.PeriodicCallback(try_exit, 100).start() 
    print("Log Server started on " + str(port))
    tornado.ioloop.IOLoop.instance().start()

