# My First PyGame, George Peterson, 11/30/2021, 2:14pm, v0.0

import pygame,sys
from pygame.locals import *

# Start Pygame
pygame.init()

# Setup the game window.
windowSurface = pygame.display.set_mode((500,400), 0, 32)
pygame.display.set_captain('Hello, world!')

# Setup color values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
CYANBLUE = (80, 255, 250)
VAMPPURP = (105, 2, 137)
