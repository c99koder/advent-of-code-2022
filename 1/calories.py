#!/usr/bin/env python3

import operator
from colorama import Fore, Style

HORIZONTAL = u'\u2500'
VERTICAL = u'\u2502'
TOP_LEFT_CORNER = u'\u250c'
TOP_RIGHT_CORNER = u'\u2510'
BOTTOM_LEFT_CORNER = u'\u2514'
BOTTOM_RIGHT_CORNER = u'\u2518'
TOP_MIDDLE = u'\u252c'
BOTTOM_MIDDLE = u'\u2534'
LEFT_MIDDLE = u'\u251c'
RIGHT_MIDDLE = u'\u2524'
MIDDLE = u'\u253c'

currentElf = 0
currentTotal = 0

totals = []

def fill_tab():
    for i in range(0,7):
        print(f'{HORIZONTAL}', end='')

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
fill_tab()
print(f'{TOP_MIDDLE}', end='')
fill_tab()
print(f'{TOP_RIGHT_CORNER}')
print(f'{VERTICAL}{Style.RESET_ALL}{Style.BRIGHT}Elf{Style.RESET_ALL}\t{Fore.YELLOW}{VERTICAL}{Style.RESET_ALL}{Style.BRIGHT}Total{Style.RESET_ALL}\t{Fore.YELLOW}{VERTICAL}')
print(f'{LEFT_MIDDLE}', end='')
fill_tab()
print(f'{MIDDLE}', end='')
fill_tab()
print(f'{RIGHT_MIDDLE}')
for total in totals:
    print(f'{VERTICAL}{Style.RESET_ALL}{total["elf"]}\t{Fore.YELLOW}{VERTICAL}{Style.RESET_ALL}{total["total"]}\t{Fore.YELLOW}{VERTICAL}')
    currentTotal += total["total"]
    count += 1
    if (count > 2):
        break
print(f'{BOTTOM_LEFT_CORNER}', end='')
fill_tab()
print(f'{BOTTOM_MIDDLE}', end='')
fill_tab()
print(f'{BOTTOM_RIGHT_CORNER}')
print(f'{Fore.CYAN}Total:\t{Style.RESET_ALL}{currentTotal}')
