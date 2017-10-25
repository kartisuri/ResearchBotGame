#!/usr/bin/env python3

import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop
import json
import os
import signal
import tornado.options
import time

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
                log_round_proposals(data)

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
    who, label = id_value.split('_')
    readable_date_time = time.ctime()
    # log_chat_txt(session, id_value, text, readable_date_time)
    file_name = join(dirname(abspath(__file__)), 'Chat_Logs_' + session + '.csv')
    if not os.path.isfile(file_name):
        with open(file_name, 'wb') as ro:
            header = 'ID,PlayerMessage,PlayerMessageTime,BotMessage,BotMessageTime\n'.encode('utf-8')
            ro.write(header)
            string = (label + ',"' + text + '",' + readable_date_time).encode('utf-8')
            ro.write(string)
    else:
        with open(file_name, 'ab') as ro:
            if who == 'Player':
                string = (label + ',"' + text + '",' + readable_date_time).encode('utf-8')
            else:
                string = (',"' + text + '",' + readable_date_time + '\n').encode('utf-8')
            ro.write(string)


def log_round_proposals(data):
    file_name = join(dirname(abspath(__file__)), 'Round_Proposals_' + data['session'] + '.csv')
    if not os.path.isfile(file_name):
        with open(file_name, 'wb') as ro:
            header = 'Round,Proposal_1,Proposal_2,Proposal_Selected,Decision,ID_Player1,ID_Player2\n'.encode('utf-8')
            ro.write(header)
            string = (data['round'] + ',' + data['proposal1'] + ',' + data['proposal2'] +
                      ',' + data['selection'] + ',' + data['decision'] + ',' +
                      data['player1'] + ',' + data['player2'] + '\n').encode('utf-8')
            ro.write(string)
    else:
        with open(file_name, 'ab') as ro:
            string = (data['round'] + ',' + data['proposal1'] + ',' + data['proposal2'] +
                      ',' + data['selection'] + ',' + data['decision'] + ',' +
                      data['player1'] + ',' + data['player2'] + '\n').encode('utf-8')
            ro.write(string)


def signal_handler(signum, frame):
    print(signum, frame)
    global is_closing
    is_closing = True


def try_exit(): 
    global is_closing
    if is_closing:
        tornado.ioloop.IOLoop.instance().stop()


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
