import shutil
import os
import sys

# get command and arguments
_, command, *args = sys.argv


def init(_):
    """
    Initializes 'zeon_fs' directory
    """
    # get directory
    cwd = os.getcwd()
    # create 'zeon_fs' directory if it isn't exists
    if not os.path.exists(cwd + '/zeon_fs'):
        os.mkdir('zeon_fs')


# try to go to the 'zeon_fs' directory
try:
    os.chdir('./zeon_fs')

except FileNotFoundError:
    pass


def list_files(_):
    """
    Returns list of files included in 'zeon_fs' directory
    """
    os.system('ls')


def add_file(path):
    """
    Copy file from given path to the 'zeon_fs' directory
    """
    source = '{}'.format(path)
    destination = '.'
    shutil.copy(source, destination)


def delete_file(file_name):
    """
    Delete file from 'zeon_fs' directory
    """
    os.remove('./{}'.format(file_name))


def get_file_content(file_name, get_file_path):
    """
    Create new file in 'zeon_fs' directory.
    The content of new file copied from file,
    that given in the path as argument
    """
    content = open(get_file_path, 'r')
    zeon_fs_file = open('./{}'.format(file_name), 'x')
    zeon_fs_file.write(content.read())
    zeon_fs_file.close()
    content.close()


# Commands Dictionary
commands = {
    'init': init,
    'add': add_file,
    'delete': delete_file,
    'list': list_files,
    'get_file': get_file_content
}

if command in commands:
    commands[command](''.join(args))
else:
    commands['get_file'](command, ''.join(args))
