#!/usr/bin/env python3

import sys
from colorama import Fore, Style
sys.path.append("../")
from utils import *

part1_sum = 0
part2_sum = 0
group_count = 0

def priority(item):
    if item >= 'a' and item <= 'z':
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27

def part1(rucksack):
    global part1_sum
    types = set()
    count = 0
    items = list(rucksack)
    for type in items:
        if count < len(rucksack) / 2:
            types.add(type)
        elif type in types:
            part1_sum += priority(type)
            return type
        count += 1

def part2(group):
    global part2_sum, group_count
    types = {}
    count = 0
    for items in group:
        for type in items:
            if type in types:
                types[type].add(count)
            else:
                types[type] = {count}
        count += 1

    badge = None

    for type, rucksacks in types.items():
        if len(rucksacks) == 3:
            badge = type
            part2_sum += priority(type)

    group_count += 1

    print(f'Group #{Fore.WHITE}{group_count}{Style.RESET_ALL}')

    for rucksack in group:
        print_rucksack(rucksack, part1(rucksack), badge)

def print_rucksack(rucksack, error, badge):
    items = list(rucksack)
    print(f'{Fore.YELLOW}{TOP_LEFT_CORNER}', end='')
    draw_line(int(len(rucksack) / 2))
    print(TOP_MIDDLE, end='')
    draw_line(int(len(rucksack) / 2))
    print(TOP_RIGHT_CORNER)

    print(f'{VERTICAL}{Style.RESET_ALL}', end='')
    count = 0
    for item in items:
        if item == error:
            print(f'{Fore.RED}{item}{Style.RESET_ALL}', end='')
        elif item == badge:
            print(f'{Fore.GREEN}{item}{Style.RESET_ALL}', end='')
        else:
            print(item, end='')
        count += 1
        if count == int(len(items) / 2):
            print(f'{Fore.YELLOW}{VERTICAL}{Style.RESET_ALL}', end='')
    print(f'{Fore.YELLOW}{VERTICAL}')

    print(BOTTOM_LEFT_CORNER, end='')
    draw_line(int(len(rucksack) / 2))
    print(BOTTOM_MIDDLE, end='')
    draw_line(int(len(rucksack) / 2))
    print(f'{BOTTOM_RIGHT_CORNER}{Style.RESET_ALL}')

window_title('Day 3: Rucksack Reorganization')
print('--- Day 3: Rucksack Reorganization ---')
group = []
for line in open('input.txt', 'r').readlines():
    line=line.rstrip()
    part1(line)
    group.append(line)
    if len(group) == 3:
        part2(group)
        group.clear()

print(f'{Fore.CYAN}Sums:{Style.RESET_ALL}\tPart 1: {Style.BRIGHT}{part1_sum}{Style.RESET_ALL}\tPart 2: {Style.BRIGHT}{part2_sum}{Style.RESET_ALL}')
