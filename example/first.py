import os


def human_read_format(size):
    formats = ['ม', 'สม', 'ฬม', 'รม']
    if size < 1024:
        return str(round(size)) + formats[0]
    size = size / 1024
    if size < 1024:
        return str(round(size)) + formats[1]
    size = size / 1024
    if size < 1024:
        return str(round(size)) + formats[2]
    size = size / 1024
    return str(round(size)) + formats[1]


def get_files_sizes():
    result = ''
    for elem in os.listdir('../'):
        result += f'{elem} {human_read_format(os.stat(elem).st_size)}\n'
    return result

