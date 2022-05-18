import sys
from commands import *

# get command and arguments
_, command, *args = sys.argv

args = ''.join(args)
if command in commands_dict.keys():
    check_args(args)
    commands_dict[command](args)
else:
    help_me()
