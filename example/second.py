import argparse


parser = argparse.ArgumentParser()
parser.add_argument('path1')
parser.add_argument('path2')
parser.add_argument('--upper', action='store_true')
parser.add_argument('--lines', default=-1)

args = parser.parse_args()

file1 = open(args.path1, encoding='utf-8', mode='r').readlines()
file2 = open(args.path2, mode='w')

n = 0
if int(args.lines) < 0:
    n = len(file1)
else:
    n = min(len(file1), int(args.lines))


for i in range(n):
    tmp = file1[i].strip('\n')
    if args.upper:
        tmp = tmp.upper()
    print(tmp, file=file2)

file2.close()
