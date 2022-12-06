#!/usr/bin/env python3
import sys
from colorama import Fore, Style
sys.path.append("../")
from utils import *

part1_sum = 0
part2_sum = 0

def draw_pairs(pairs):
    global part1_sum, part2_sum
    assignments = {}
    count = 0
    contained = ""
    overlap = False

    for pair in pairs:
        r = pair.split('-')

        for i in range(int(r[0]), int(r[1])+1):
            if i in assignments:
                assignments[i] = 'X'
            else:
                assignments[i] = count

        count += 1

    p0 = pairs[0].split('-')
    p1 = pairs[1].split('-')
    if (int(p0[0]) <= int(p1[0]) and int(p0[1]) >= int(p1[1])) or (int(p1[0]) <= int(p0[0]) and int(p1[1]) >= int(p0[1])):
        part1_sum += 1
        contained = f'{Fore.MAGENTA}(Fully Contained)'

    print(f'{Fore.YELLOW}{TOP_LEFT_CORNER}', end='')
    draw_line(100)
    print(f'{TOP_RIGHT_CORNER}')

    print(f'{VERTICAL}{Style.RESET_ALL}', end='')

    for i in range(1, 101):
        if i in assignments:
            if assignments[i] == 'X':
                print(Fore.RED, end='')
                overlap = True
            elif assignments[i] == 1:
                print(Fore.BLUE, end='')
            else:
                print(Fore.GREEN, end='')
        else:
            print(f'{Style.RESET_ALL}', end='')

        print(SQUARE, end='')
    print(f'{Fore.YELLOW}{VERTICAL} {Fore.CYAN}{pairs[0]}, {pairs[1]} {contained} {Fore.YELLOW}')

    print(BOTTOM_LEFT_CORNER, end='')
    draw_line(100)
    print(f'{BOTTOM_RIGHT_CORNER}{Style.RESET_ALL}')

    if overlap:
        part2_sum += 1

print('--- Day 4: Camp Cleanup ---')

for line in open('input.txt', 'r').readlines():
    line = line.rstrip().split(',')
    draw_pairs(line)

print(f'{Fore.CYAN}Sums:{Style.RESET_ALL}\tPart 1: {Style.BRIGHT}{part1_sum}{Style.RESET_ALL}\tPart 2: {Style.BRIGHT}{part2_sum}{Style.RESET_ALL}')
