import sys
from commands import *

# get command and arguments
_, command, *args = sys.argv


def check_args():
    if len(args) > 0:
        return True
    else:
        print('Here is no arguments!')
        return None


args = ''.join(args)

if command in commands:
    check_args()
    commands[command](args)
else:
    commands['get_file'](args)
