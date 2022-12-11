#!/usr/bin/env python3
import sys
from colorama import Fore, Style
sys.path.append("../")
from utils import *

cycle_count = 0
register_x = 1
signal_check = 20
part1_sum = 0
CRT_WIDTH = 40
CRT_HEIGHT = 6
crt_x = 0
crt_y = 0

def cycle():
    global cycle_count, register_x, signal_check, part1_sum, crt_x, crt_y
    cycle_count += 1
    signal_check -= 1

    print(Fore.GREEN, end = '')

    if crt_x >= register_x - 1 and crt_x <= register_x + 1:
        print(f'{Style.BRIGHT}{BLOCK}{BLOCK}{Style.RESET_ALL}', end='')
    else:
        print(f'{Style.DIM}{BLOCK}{BLOCK}{Style.RESET_ALL}', end='')

    crt_x += 1
    if crt_x == CRT_WIDTH:
        crt_x = 0
        crt_y += 1
        print(Style.RESET_ALL)

    if crt_y == CRT_HEIGHT:
        crt_y = 0
        print(Style.RESET_ALL)

    if signal_check == 0:
        part1_sum += cycle_count * register_x
        signal_check = 40

window_title('Day 10: Cathode-Ray Tube')
print('--- Day 10: Cathode-Ray Tube ---')

for line in open('input.txt', 'r').readlines():
    line = line.rstrip().split()

    cycle()

    if line[0] == 'addx':
        cycle()
        register_x += int(line[1])

print(f'{Fore.CYAN}Part 1:{Style.RESET_ALL}\t{part1_sum}')
