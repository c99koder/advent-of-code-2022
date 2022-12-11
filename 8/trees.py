#!/usr/bin/env python3
import sys, operator
from colorama import Fore, Style
sys.path.append("../")
from utils import *

heights = []

def is_visible(x: int, y: int):
    global heights

    height = len(heights)
    width = len(heights[y])

    if x == 0 or y == 0 or y == height - 1 or x == width - 1:
        return True

    for x1 in range(x + 1, width):
        if heights[y][x1] >= heights[y][x]:
            break
        elif x1 == width - 1:
            return True

    for x1 in reversed(range(0, x)):
        if heights[y][x1] >= heights[y][x]:
            break
        elif x1 == 0:
            return True

    for y1 in range(y + 1, height):
        if heights[y1][x] >= heights[y][x]:
            break
        elif y1 == height - 1:
            return True

    for y1 in reversed(range(0, y)):
        if heights[y1][x] >= heights[y][x]:
            break
        elif y1 == 0:
            return True

    return False

def scenic_score(x: int, y: int):
    global heights

    height = len(heights)
    width = len(heights[y])

    left = 0
    right = 0
    up = 0
    down = 0

    for x1 in range(x + 1, width):
        right += 1
        if heights[y][x1] >= heights[y][x]:
            break

    for x1 in reversed(range(0, x)):
        left += 1
        if heights[y][x1] >= heights[y][x]:
            break

    for y1 in range(y + 1, height):
        down += 1
        if heights[y1][x] >= heights[y][x]:
            break

    for y1 in reversed(range(0, y)):
        up += 1
        if heights[y1][x] >= heights[y][x]:
            break

    return left * right * up * down

window_title('Day 8: Treetop Tree House')
print('--- Day 8: Treetop Tree House ---')

for line in open('input.txt', 'r').readlines():
    line = line.rstrip()
    row = []

    for h in line:
        row.append(int(h))
    
    heights.append(row)

scores = []
for y in range(len(heights)):
    for x in range(len(heights[y])):
        scores.append({'x': x, 'y': y, 'score': scenic_score(x, y)})

scores = sorted(scores, key=operator.itemgetter('score'), reverse=True)

visible_count = 0
for y in range(len(heights)):
    for x in range(len(heights[y])):
        if x == scores[0]["x"] and y == scores[0]["y"]:
            print(f'{Fore.WHITE}', end = '')
        elif is_visible(x, y):
            print(f'{Fore.GREEN}', end = '')
            visible_count += 1
        else:
            print(f'{Fore.RED}', end = '')
        print('*', end = '')
    print(Style.RESET_ALL)

print(f'{Fore.CYAN}Visible trees: {Fore.YELLOW}{visible_count}\t{Fore.CYAN}Best scenic score: {Fore.YELLOW}{scores[0]["score"]} {Fore.WHITE}({scores[0]["x"]},{scores[0]["y"]})')