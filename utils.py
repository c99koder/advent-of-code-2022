from colorama import Fore, Style, Back

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
BLOCK = u'\u2588'
SQUARE = u'\u25aa'
CLEAR_SCREEN = '\033[H\033[J'
ARROW_RIGHT = '\u2192'
ARROW_LEFT = '\u2190'
ARROW_DOWN = '\u2193'
ARROW_UP = '\u2191'
DIAMOND = '\u2b29'

def draw_line(length: int):
    print(HORIZONTAL*length, end='')

def window_title(title: str):
    print(f'\033]0;{title}\007')

def strip(string: str):
    for key in Style.__dict__.keys():
        string = string.replace(Style.__dict__[key], '')
    for key in Fore.__dict__.keys():
        string = string.replace(Fore.__dict__[key], '')
    for key in Back.__dict__.keys():
        string = string.replace(Fore.__dict__[key], '')
    return string