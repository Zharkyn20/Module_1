import sys
from commands import *

# get command and arguments
_, command, *args = sys.argv

args = ''.join(args)

if command in commands:
    check_args(args)
    commands[command](args)
else:
    commands['get_file'](args)
