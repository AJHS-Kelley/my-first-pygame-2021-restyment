# My First PyGame, George Peterson, 11/30/2021, 2:14pm, v0.0

import pygame,sys
from pygame.locals import *

# Start Pygame
pygame.init()

# Setup the game window.
windowSurface = pygame.display.set_mode((500,400), 0, 32)
pygame.display.set_captain('Hello, world!')