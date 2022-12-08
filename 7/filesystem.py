#!/usr/bin/env python3
import sys, operator
from colorama import Fore, Style
sys.path.append("../")
from utils import *

filesystem = {}
cwd = '/'
part1_sum = 0
part2 = []

FS_TOTAL = 70000000
UPDATE_SIZE = 30000000

def get_path(path: str):
    global filesystem
    c = filesystem
    if path == '/':
        return c

    path = path.split('/')
    path.remove('')
    
    for d in path:
        if not d in c:
            c[d] = {}
        c = c[d]

    return c

def print_dir(dir: dict, name: str, level: int):
    global part1_sum, amount_to_free
    size = dir_size(dir)
    if size <= 100000:
        part1_sum += size
    if size >= amount_to_free:
        part2.append({'name': name, 'size': size})

    if level > 0:
        print(' '*(level*2), end='')
    print(f'{Fore.YELLOW}- {Fore.MAGENTA}{name} {Fore.GREEN}(dir)')

    for k in dir.keys():
        if type(dir[k]) is dict:
            print_dir(dir[k], k, level + 1)
        else:
            print(' '*((level+1)*2), end='')
            print(f'{Fore.YELLOW}- {Fore.CYAN}{k} {Fore.GREEN}(file, size={Fore.BLUE}{dir[k]}{Fore.GREEN})')

def dir_size(dir: dict):
    size = 0
    for k in dir.keys():
        if type(dir[k]) is dict:
            size += dir_size(dir[k])
        else:
            size += dir[k]

    return size

print('--- Day 7: No Space Left On Device ---')

for line in open('input.txt', 'r').readlines():
    line = line.rstrip().split()

    if line[0] == '$':
        print(f'{Fore.BLUE}[{Fore.WHITE}{cwd}{Fore.BLUE}]{Fore.RED} $ {Fore.GREEN}{line[1]}', end = '')
        if len(line) > 2:
            print(f' {Fore.CYAN}{line[2]}', end = '')
        print(Style.RESET_ALL)

        if line[1] == 'cd':
            if line[2].startswith('/'):
                cwd = line[2]
            elif line[2] == '..':
                path = cwd.split('/')
                path.remove('')
                path.pop()
                cwd = '/' + '/'.join(path)
            else:
                if not cwd.endswith('/'):
                    cwd += '/'
                cwd += line[2]
    elif line[0] == 'dir':
        print(f'{Fore.YELLOW}{line[0]} {Fore.WHITE}{line[1]}{Style.RESET_ALL}')
        dir = cwd
        if not dir.endswith('/'):
            dir += '/'
        dir += line[1]
        get_path(dir)
    elif line[0].isdigit():
        print(f'{Fore.MAGENTA}{line[0]} {Fore.WHITE}{line[1]}{Style.RESET_ALL}')
        get_path(cwd)[line[1]] = int(line[0])

print()
print('Filesystem:')

FS_FREE = FS_TOTAL - dir_size(filesystem)
amount_to_free = UPDATE_SIZE - FS_FREE

print_dir(filesystem, '/', 0)
print(f'{Fore.YELLOW}Total size: {Fore.GREEN}{dir_size(filesystem)} {Fore.YELLOW}Free space: {Fore.RED}{FS_FREE} {Fore.YELLOW}Amount to free: {Fore.MAGENTA}{amount_to_free}')

print(f'{Fore.CYAN}Part 1: {Style.RESET_ALL}{part1_sum}')
part2 = sorted(part2, key=operator.itemgetter('size'))
print(f'{Fore.CYAN}Part 2: {Style.RESET_ALL}{part2[0]["size"]}')