#!/usr/bin/env python3
import sys, math
from colorama import Fore, Back, Style
sys.path.append("../")
from utils import *

window_title('Day 12: Hill Climbing Algorithm')
print('--- Day 12: Hill Climbing Algorithm ---')

class Cell:
    def __init__(self, height = 0, pos = None):
        self.height = height
        self.count = math.inf
        self.path_from = None
        self.pos = pos

    def key(self):
        return str(self.pos[0]) + '-' + str(self.pos[1])

map = []

def get_cell(pos):
    global map
    return map[pos[1]][pos[0]]

def add_point(a,b):
    return [a[0] + b[0], a[1] + b[1]]

# Python implementation of Dijkstra's Algorithm from https://github.com/mortoray/path-finding
def shortest(start):
    visited = set()

    for y in range(0,len(map)):
        for x in range(0, len(map[y])):
            map[y][x].count = math.inf
            map[y][x].path_from = None

    open_list = [start]
    get_cell(open_list[0]).count = 0
    neighbours = [ [-1,0], [1,0], [0,-1], [0,1] ]
    while open_list:
        last_pos = open_list.pop(0)
        last_cell = get_cell(last_pos)

        for neighbor in neighbours:
            ncell_pos = add_point(last_pos, neighbor)

            if ncell_pos[0] < 0 or ncell_pos[1] < 0 or ncell_pos[1] >= len(map) or ncell_pos[0] >= len(map[ncell_pos[1]]):
                continue

            cell = get_cell(ncell_pos)

            if cell.height - last_cell.height > 1:
                continue

            dist = last_cell.count + 1

            if cell.count > dist:
                cell.count = dist
                cell.path_from = last_cell
                open_list.append(ncell_pos)

    cell = get_cell([end_x, end_y])
    while cell != None:
        visited.add(cell.key())
        cell = cell.path_from

    return visited

visited = set()
start_x = None
start_y = None
end_x = None
end_y = None

def print_map():
    global visited, map
    print(f'{Fore.YELLOW}{TOP_LEFT_CORNER}{HORIZONTAL*len(map[0])}{TOP_RIGHT_CORNER}')
    for y in range(0,len(map)):
        print(f'{Fore.YELLOW}{VERTICAL}', end='')
        for x in range(0, len(map[y])):
            if map[y][x].height < 2:
                print(f'{Back.GREEN}', end='')
            elif map[y][x].height == 2:
                print(f'{Back.LIGHTGREEN_EX}', end='')
            else:
                c = max([min([231 + map[y][x].height, 255]), 232])
                print(f'\033[48;5;{c}m', end='')

            if x == end_x and y == end_y:
                print(f'{Fore.CYAN}{DIAMOND}', end='')
            elif str(x) + '-' + str(y) in visited:
                print(f'{Fore.RED}{DIAMOND}', end='')
            else:
                print(' ', end='')
        print(f'{Style.RESET_ALL}{Fore.YELLOW}{VERTICAL}')
    print(f'{Fore.YELLOW}{BOTTOM_LEFT_CORNER}{HORIZONTAL*len(map[0])}{BOTTOM_RIGHT_CORNER}{Style.RESET_ALL}')

y = 0
for line in open('input.txt', 'r').readlines():
    line = line.rstrip()

    map.append([])

    for x in range(len(line)):
        if line[x] == 'S':
            start_x = x
            start_y = y
            map[y].append(Cell(height=0, pos=[x, y]))
        elif line[x] == 'E':
            end_x = x
            end_y = y
            map[y].append(Cell(height=25, pos=[x, y]))
        else:
            map[y].append(Cell(height=ord(line[x]) - ord('a'), pos=[x, y]))

    y += 1

part1 = len(shortest([start_x, start_y])) - 1

part2 = []
for y in range(0,len(map)):
    for x in range(0, len(map[y])):
        if map[y][x].height == 0:
            route = shortest([x, y])
            if len(route) > 1:
                part2.append(route)

part2 = sorted(part2, key=len)
visited = part2[0]
print_map()
print(f'Part 1 route: {Fore.CYAN}{part1} steps{Style.RESET_ALL}\tPart 2 route: {Fore.CYAN}{len(visited) - 1} steps{Style.RESET_ALL}')
