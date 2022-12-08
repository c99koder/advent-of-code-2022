#!/usr/bin/env python3

import operator, sys
from colorama import Fore, Style
sys.path.append("../")
from utils import *

currentElf = 0
currentTotal = 0

totals = []

window_title('Day 1: Calorie Counting')
print('--- Day 1: Calorie Counting ---')
for line in open('input.txt', 'r').readlines():
    line=line.rstrip()
    if line.isnumeric():
        currentTotal+=int(line)
    else:
        totals.append({'elf': currentElf, 'total': currentTotal})
        currentElf += 1
        currentTotal = 0

totals = sorted(totals, key=operator.itemgetter('total'), reverse=True)

count = 0
currentTotal = 0

print(f'{Fore.YELLOW}{TOP_LEFT_CORNER}', end='')
draw_line(7)
print(f'{TOP_MIDDLE}', end='')
draw_line(7)
print(f'{TOP_RIGHT_CORNER}')
print(f'{VERTICAL}{Style.RESET_ALL}{Style.BRIGHT}Elf{Style.RESET_ALL}\t{Fore.YELLOW}{VERTICAL}{Style.RESET_ALL}{Style.BRIGHT}Total{Style.RESET_ALL}\t{Fore.YELLOW}{VERTICAL}')
print(f'{LEFT_MIDDLE}', end='')
draw_line(7)
print(f'{MIDDLE}', end='')
draw_line(7)
print(f'{RIGHT_MIDDLE}')
for total in totals:
    print(f'{VERTICAL}{Style.RESET_ALL}{total["elf"]}\t{Fore.YELLOW}{VERTICAL}{Style.RESET_ALL}{total["total"]}\t{Fore.YELLOW}{VERTICAL}')
    currentTotal += total["total"]
    count += 1
    if (count > 2):
        break
print(f'{BOTTOM_LEFT_CORNER}', end='')
draw_line(7)
print(f'{BOTTOM_MIDDLE}', end='')
draw_line(7)
print(f'{BOTTOM_RIGHT_CORNER}')
print(f'{Fore.CYAN}Total:\t{Style.RESET_ALL}{currentTotal}')
