#!/usr/bin/env python3

part1_sum = 0
part2_sum = 0

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
            break
        count += 1

def part2(group):
    global part2_sum
    types = {}
    count = 0
    for items in group:
        for type in items:
            if type in types:
                types[type].add(count)
            else:
                types[type] = {count}
        count += 1

    for type, rucksacks in types.items():
        if len(rucksacks) == 3:
            part2_sum += priority(type)

print('--- Day 3: Rucksack Reorganization ---')
group = []
for line in open('input.txt', 'r').readlines():
    line=line.rstrip()
    part1(line)
    group.append(line)
    if len(group) == 3:
        part2(group)
        group.clear()

print(f'Sums:\tPart 1: {part1_sum}\tPart 2: {part2_sum}')
