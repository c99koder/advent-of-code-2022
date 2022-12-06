#!/usr/bin/env python3
import sys
from colorama import Fore, Style
sys.path.append("../")
from utils import *

stacks_part1 = {}
stacks_part2 = {}

def parse_drawing(line):
    global stacks_part1, stacks_part2
    pos = 0

    for c in line:
        if c != ' ' and c != '[' and c != ']':
            i = int((pos-1)/4)
            if i in stacks_part1:
                stacks_part1[i].insert(0, c)
            else:
                stacks_part1[i] = [c]

        pos += 1

    stacks_part2 = {key: value[:] for key, value in stacks_part1.items()}

def parse_move(line):
    if len(line) > 1 and line[0] == 'move':
        count = int(line[1])
        src = int(line[3]) - 1
        dst = int(line[5]) - 1

        boxes_part1 = []
        boxes_part2 = []
        for i in range(0, count):
            boxes_part1.append(stacks_part1[src].pop())
            boxes_part2.insert(0, stacks_part2[src].pop())

        stacks_part1[dst].extend(boxes_part1)
        stacks_part2[dst].extend(boxes_part2)

def draw_stacks(stacks):
    for stack in range(0, len(stacks)):
        print(f'{Fore.YELLOW}{stack+1}: {Fore.RED}', end='')
        for box in stacks[stack][:-1]:
            print(f'[{box}]', end='')
        print(f'{Fore.GREEN}[{stacks[stack][len(stacks[stack])-1]}]{Style.RESET_ALL}')

print('--- Day 5: Supply Stacks ---')

for line in open('input.txt', 'r').readlines():
    line = line.rstrip()
    if '[' in line:
        parse_drawing(line)
    else:
        parse_move(line.split())

top = ""
for stack in range(0, len(stacks_part1)):
    top += stacks_part1[stack][len(stacks_part1[stack])-1]

draw_stacks(stacks_part1)
print(f'{Fore.CYAN}Part 1:{Style.RESET_ALL}\t{Style.BRIGHT}{top}{Style.RESET_ALL}\n')

top = ""
for stack in range(0, len(stacks_part2)):
    top += stacks_part2[stack][len(stacks_part2[stack])-1]
draw_stacks(stacks_part2)
print(f'{Fore.CYAN}Part 2:{Style.RESET_ALL}\t{Style.BRIGHT}{top}{Style.RESET_ALL}\n')

