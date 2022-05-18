import shutil
import os


def check_args(args):
    if len(args) > 0:
        return True
    else:
        print('Here is no arguments!')
        return None


def help_me():
    help_text = " Available commands: \
    'init': , \
    'add': arguments -path, \
    'delete': arguments -file_name, \
    'list': , \
    'get': arguments -file_name, -path \
    "
    print(help_text)


def init(_):
    """
    Initializes 'zeon_fs' directory
    """
    cwd = os.getcwd()
    if os.path.exists(cwd + '/zeon_fs'):
        print("Path exists")
        return None

    os.mkdir('zeon_fs')


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
    source = f'{path}'
    destination = '.'
    shutil.copy(source, destination)


def delete_file(file_name):
    """
    Delete file from 'zeon_fs' directory
    """
    os.remove(f'./{file_name}')


def get_file(file_name, get_file_path):
    """
    Create new file in 'zeon_fs' directory.
    The content of new file copied from file,
    that given in the path as argument
    """
    content = open(get_file_path, 'r')
    zeon_fs_file = open(f'./{file_name}', 'x')
    zeon_fs_file.write(content.read())
    zeon_fs_file.close()
    content.close()


# Commands Dictionary
commands_dict = {
    'init': init,
    'add': add_file,
    'delete': delete_file,
    'list': list_files,
    'get': get_file,
}
