#!/usr/bin/env python3
import sys
from colorama import Fore, Style
sys.path.append("../")
from utils import *

GUIDE = {'A': 'rock', 'B': 'paper', 'C': 'scissors', 'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
SCORES = {'rock': 1, 'paper': 2, 'scissors': 3}
WINNERS = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
LOSERS = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
COLORS = {'rock': Style.DIM, 'paper': Style.BRIGHT, 'scissors': Style.DIM + Fore.YELLOW}

DRAW_BONUS = 3
WIN_BONUS = 6

score_part1 = 0
score_part2 = 0

def part1(opponent, player):
    global score_part1

    score_part1 += SCORES[player]

    out = f'{Fore.YELLOW}{VERTICAL}{Style.RESET_ALL}'
    out += f'{COLORS[opponent]}{opponent.rjust(9, " ")}{Style.RESET_ALL} vs. {COLORS[player]}{player}{Style.RESET_ALL}: '

    if opponent == player:
        score_part1 += DRAW_BONUS
        out += f'DRAW'
    elif opponent == WINNERS[player]:
        score_part1 += WIN_BONUS
        out += f'{Fore.GREEN}WIN{Style.RESET_ALL}'
    else:
        out += f'{Fore.RED}LOSE{Style.RESET_ALL}'

    stripped = strip(out)

    if len(stripped) < 30:
        out += ' '*(30 - len(stripped))

    print(out, end='')

def part2(opponent, outcome):
    global score_part2
    if outcome == 'X': #Lose
        player = WINNERS[opponent]
    elif outcome == 'Y': #Draw
        player = opponent
    elif outcome == 'Z': #Win
        player = LOSERS[opponent]

    score_part2 += SCORES[player]

    out = f'{Fore.YELLOW}{VERTICAL}{Style.RESET_ALL}'
    out += f'{COLORS[opponent]}{opponent.rjust(9, " ")}{Style.RESET_ALL} vs. {COLORS[player]}{player}{Style.RESET_ALL}: '

    if opponent == player:
        score_part2 += DRAW_BONUS
        out += f'DRAW'
    elif opponent == WINNERS[player]:
        score_part2 += WIN_BONUS
        out += f'{Fore.GREEN}WIN{Style.RESET_ALL}'
    else:
        out += f'{Fore.RED}LOSE{Style.RESET_ALL}'

    stripped = strip(out)

    if len(stripped) < 30:
        out += ' '*(30 - len(stripped))

    out += f'{Fore.YELLOW}{VERTICAL}'

    print(out)

print('--- Day 2: Rock Paper Scissors ---')

print(f'{Fore.YELLOW}{TOP_LEFT_CORNER}', end='')
draw_line(29)
print(TOP_MIDDLE, end='')
draw_line(29)
print(TOP_RIGHT_CORNER)

print(f'{VERTICAL}{Style.RESET_ALL}{Style.BRIGHT}{"Method 1".center(29, " ")}{Style.RESET_ALL}{Fore.YELLOW}', end='')
print(f'{VERTICAL}{Style.RESET_ALL}{Style.BRIGHT}{"Method 2".center(29, " ")}{Style.RESET_ALL}{Fore.YELLOW}{VERTICAL}')

for line in open('input.txt', 'r').readlines():
    line = line.rstrip().split()
    part1(GUIDE[line[0]], GUIDE[line[1]])
    part2(GUIDE[line[0]], line[1])

print(BOTTOM_LEFT_CORNER, end='')
draw_line(29)
print(BOTTOM_MIDDLE, end='')
draw_line(29)
print(f'{BOTTOM_RIGHT_CORNER}{Style.RESET_ALL}')

print(f'{Fore.CYAN}Final scores:{Style.RESET_ALL}\tpart 1: {Style.BRIGHT}{score_part1}{Style.RESET_ALL}\tpart 2: {Style.BRIGHT}{score_part2}{Style.RESET_ALL}')

