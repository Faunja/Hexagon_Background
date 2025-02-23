# variables.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
import pygame

pygame.init()
DISPLAYSURF = pygame.display.get_desktop_sizes()
SCREEN_WIDTH, SCREEN_HEIGHT = DISPLAYSURF[0]
SCREEN_WIDTH = round(SCREEN_WIDTH * 3/4)
SCREEN_HEIGHT = round(SCREEN_HEIGHT * 3/4)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

White = (255, 255, 255)
darkGray = (45, 45, 45)
Black = (0, 0, 0)

# Determines the time, and how fast it runs.
FPS = 60
clock = pygame.time.Clock()