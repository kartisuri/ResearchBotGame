import os
from os.path import abspath, dirname, join

directory = join(dirname(abspath(__file__)))
base_command = r'start /B start cmd.exe @cmd /k '
# command1 = "pip3 install -U numpy tornado requests otree-core && npm install -g pb-node"
command2 = base_command + 'python "' + directory + r'"\LogServer.py'
command3 = base_command + 'node "' + directory + r'"\chatbot.js'
command4 = base_command + 'cd "' + directory + '"'
# os.system(command1)
os.system(command2)
os.system(command3)
os.system(command4)
