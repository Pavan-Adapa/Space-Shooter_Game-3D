from pyray import *
from raylib import *
from random import randint, uniform, choice
from os.path import join
from custom_timer import Timer

WINDOW_WIDTH, WINDOW_HEIGHT = 1820, 980
BG_COLOR = BLACK
PLAYER_SPEED = 7
LASER_SPEED = 9
METEOR_SPEED_RANGE = [4, 5]
METEOR_TIMER_DURATION = 0.4
FONT_SIZE = 100
FONT_PADDING = 60
