import os

while True:
    value = input('>>> ').split()
    if value[0].upper() == 'EXIT':
        break

    os.system('{} {}'.format(value[0], value[1]))

