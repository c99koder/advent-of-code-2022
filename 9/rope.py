#!/usr/bin/env python3
import sys
sys.path.append("../")
from utils import *

MAX = 20
KNOTS = 2

knots_x = [int(MAX/2)] * KNOTS
knots_y = [int(MAX/2)] * KNOTS
part1_visited = [False]*(MAX*MAX)
part1 = 0

def draw():
    global knots_x, knots_y

    for y in range(0, MAX):
        for x in range(0, MAX):
            drawn = False
            for knot in range(0, KNOTS):
                if x == knots_x[knot] and y == knots_y[knot]:
                    drawn = True
                    if knot == 0:
                        print('H', end = '')
                    elif knot == KNOTS - 1:
                        print('T', end = '')
                    else:
                        print(knot, end = '')
                    break

            if not drawn:
                print('.', end = '')
        print()

def move(dx: int, dy: int):
    global knots_x, knots_y, part1_visited, part1

    knots_x[0] += dx
    knots_y[0] += dy

    for knot in range(1, KNOTS):
        if max(knots_x[knot-1], knots_x[knot]) - min(knots_x[knot-1], knots_x[knot]) > 1:
            knots_x[knot] = knots_x[knot-1] - dx
            knots_y[knot] = knots_y[knot-1]

        if max(knots_y[knot-1], knots_y[knot]) - min(knots_y[knot-1], knots_y[knot]) > 1:
            knots_y[knot] = knots_y[knot-1] - dy
            knots_x[knot] = knots_x[knot-1]

    if part1_visited[knots_y[1] * MAX + knots_x[1]] == False:
        part1 += 1
        part1_visited[knots_y[1] * MAX + knots_x[1]] = True

window_title('Day 9: Rope Bridge')
print('--- Day 9: Rope Bridge ---')

for line in open('input.txt', 'r').readlines():
    line = line.rstrip().split()

    print(f'== {line[0]} {line[1]} ==\n')

    for i in range(0, int(line[1])):
        if line[0] == 'U':
            move(0, -1)
        if line[0] == 'D':
            move(0, 1)
        if line[0] == 'L':
            move(-1, 0)
        if line[0] == 'R':
            move(1, 0)

        draw()
        print()

print(f'Part 1: {part1}')