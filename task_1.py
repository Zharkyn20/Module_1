import os

while True:
    value = input('>>> ').split()
    if value[0].upper() == 'EXIT':
        break

    if value[0] == 'touch':
        os.system('touch {}'.format(value[1]))
    elif value[0] == 'rm':
        os.system('rm {}'.format(value[1]))
    elif value[0] == 'less':
        os.system('less {}'.format(value[1]))

