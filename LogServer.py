#!/usr/bin/env python3

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
        self.write("Welcome to Game Log Server")
    
    def post(self):
        data = {'round_proposals': ''}
        if self.request.body:
            print("Got JSON data: ", self.request.body)
            data = json.loads(self.request.body)
            key, value = list(data['round_proposals'].items())[0]
            print(key + ': ' + str(value))
            log_round_proposals(key, str(value))
            self.write('Round proposal logged')
            self.finish()
 
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [(r'/', IndexPageHandler)]
        settings = {'template_path': 'templates'}
        tornado.web.Application.__init__(self, handlers, **settings)
		
def log_round_proposals(round, proposals):
    file_name = join(dirname(abspath(__file__)), 'round_options.txt')
    if round == '1':
        with open(file_name, 'w') as ro:
            string = 'Round1 Proposals: ' + proposals + '\n'
            ro.write(string)
    else:
        with open(file_name, 'a') as ro:
            string = 'Round' + round + ' Proposals: ' + proposals + '\n'
            ro.write(string)

def signal_handler(signum, frame):
    global is_closing
    is_closing = True

def try_exit(): 
    global is_closing
    if is_closing:
        tornado.ioloop.IOLoop.instance().stop()

def test_log():
    log_round_proposals('1', str(['a', 'b']))
    log_round_proposals('2', str(['c', 'd']))

#test_log()	

if __name__ == '__main__':
    tornado.options.parse_command_line()
    signal.signal(signal.SIGINT, signal_handler)
    port = 6000
    ws_app = Application()
    server = tornado.httpserver.HTTPServer(ws_app)
    server.listen(port)
    tornado.ioloop.PeriodicCallback(try_exit, 100).start() 
    print("Game Log Server started on " + str(port))
    tornado.ioloop.IOLoop.instance().start()
