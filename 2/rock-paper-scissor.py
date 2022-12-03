#!/usr/bin/env python3

GUIDE = {'A': 'rock', 'B': 'paper', 'C': 'scissors', 'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
SCORES = {'rock': 1, 'paper': 2, 'scissors': 3}
WINNERS = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
LOSERS = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}

DRAW_BONUS = 3
WIN_BONUS = 6

score_part1 = 0
score_part2 = 0

print('--- Day 2: Rock Paper Scissors ---')

def part1(opponent, player):
    global score_part1

    score_part1 += SCORES[player]

    if opponent == player:
        score_part1 += DRAW_BONUS
    elif opponent == WINNERS[player]:
        score_part1 += WIN_BONUS

def part2(opponent, outcome):
    global score_part2
    if outcome == 'X': #Lose
        player = WINNERS[opponent]
    elif outcome == 'Y': #Draw
        player = opponent
    elif outcome == 'Z': #Win
        player = LOSERS[opponent]

    score_part2 += SCORES[player]

    if opponent == player:
        score_part2 += DRAW_BONUS
    elif opponent == WINNERS[player]:
        score_part2 += WIN_BONUS

for line in open('input.txt', 'r').readlines():
    line = line.rstrip().split()
    part1(GUIDE[line[0]], GUIDE[line[1]])
    part2(GUIDE[line[0]], line[1])

print(f'Final scores:\tpart 1: {score_part1}\tpart 2:{score_part2}')
