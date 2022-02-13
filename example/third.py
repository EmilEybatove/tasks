import argparse

parser = argparse.ArgumentParser()
parser.add_argument('name', nargs='*')
parser.add_argument('--count', action='store_true')
parser.add_argument('--num', action='store_true')
parser.add_argument('--sort', action='store_true')

args = parser.parse_args()

try:
    if len(args.name) != 1:
        raise Exception
    name = args.name[0]
    file = open(name, encoding='utf-8').readlines()
    if args.sort:
        file.sort()
    for i in range(len(file)):
        if args.num:
            print(i, end=' ')
        print(file[i].strip('\n'))
    if args.count:
        print(f'rows count: {len(file)}')
except Exception:
    print('ERROR')
