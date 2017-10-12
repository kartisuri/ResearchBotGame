import os
from os.path import abspath, dirname, join

directory = join(dirname(abspath(__file__)))
base_command = r"start /B start cmd.exe @cmd /k "
command1 = base_command + "python " + directory + r"\LogServer.py"
command2 = "cd " + directory + " && otree.exe runserver"
os.system(command1)
os.system(command2)
