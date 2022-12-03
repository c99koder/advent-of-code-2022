#!/usr/bin/env python3

import operator

currentElf = 0
currentTotal = 0

totals = []

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

print('Elf\tTotal')
for total in totals:
    print(f'{total["elf"]}\t{total["total"]}')
    currentTotal += total["total"]
    count += 1
    if (count > 2):
        break
print(f'Total:\t{currentTotal}')
