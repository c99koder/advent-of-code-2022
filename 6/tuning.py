#!/usr/bin/env python3
import sys
from colorama import Fore, Style
sys.path.append("../")
from utils import *

def find_marker(line, length):
    for offset in range(length, len(line)):
        chars = {}
        match = True
        for i in range(0,length):
            if line[offset - i] in chars:
                match = False
                break
            chars[line[offset - i]] = True

        if match:
            return(offset + 1)

    return -1

window_title('Day 6: Tuning Trouble')
print('--- Day 6: Tuning Trouble ---')
line = open('input.txt', 'r').readlines()[0]

packet_offset = find_marker(line, 4)
message_offset = find_marker(line, 14)

print(f'Start of packet offset: {Fore.CYAN}{packet_offset}{Style.RESET_ALL} Marker: {Fore.YELLOW}{line[packet_offset - 4:packet_offset]}{Style.RESET_ALL}')
print(f'Start of message offset: {Fore.CYAN}{message_offset}{Style.RESET_ALL} Marker: {Fore.YELLOW}{line[message_offset - 14:message_offset]}{Style.RESET_ALL}')