# background.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
import pygame, random
from variables import *

backHexagon = (random.randint(0, 195), random.randint(0, 195), random.randint(0, 195))
frontHexagon = (backHexagon[0] + 60, backHexagon[1] + 60, backHexagon[2] + 60)

def draw_hexagon(x, y, hexagon_radius):
    straight_x = hexagon_radius * (4 / 5)
    corner_x = straight_x / 2
    corner_y = straight_x * (3 ** (1/2) / 2)
    pygame.draw.polygon(screen, frontHexagon, ((x + corner_x, y + corner_y), (x + straight_x, y), (x + corner_x, y - corner_y), (x - corner_x, y - corner_y), (x - straight_x, y), (x - corner_x, y + corner_y)))

def draw_background_hexagon(x, y, hexagon_radius):
    straight_x = hexagon_radius
    corner_x = straight_x / 2
    corner_y = straight_x * (3 ** (1/2) / 2)
    pygame.draw.polygon(screen, backHexagon, ((x + corner_x, y + corner_y), (x + straight_x, y), (x + corner_x, y - corner_y), (x - corner_x, y - corner_y), (x - straight_x, y), (x - corner_x, y + corner_y)))
    draw_hexagon(x, y, hexagon_radius)

def draw_background(cameraPosition, cameraPerspective):
    center_x = round(SCREEN_WIDTH / 2) + cameraPosition[0]
    center_y = round(SCREEN_HEIGHT / 2) + cameraPosition[1]

    # Define the Radius of the hexagon
    hexagon_radius = SCREEN_WIDTH / 32 / cameraPerspective
    # Calculates the distance between hexagons
    x_distance = hexagon_radius * (3 / 2)
    y_distance = hexagon_radius * (3 ** (1/2) / 2)
    # Calculates the cutoff distance of hexagons
    x_cutoff = [SCREEN_WIDTH + x_distance, -x_distance]
    y_cutoff = [SCREEN_HEIGHT + y_distance, -y_distance]

    x_offset = round(cameraPosition[0] / x_distance)
    y_offset = round(cameraPosition[1] / y_distance)
    if y_offset % 2 != 0:
        y_offset += 1
    x_repeat = round(SCREEN_WIDTH / x_distance)
    y_repeat = round(SCREEN_HEIGHT / y_distance)
    if y_repeat % 2 != 0:
        y_repeat += 1
    
    screen.fill(White)
    for x in range(-x_repeat - x_offset, x_repeat + 1 - x_offset):
        x_position = center_x + x_distance * x
        if x_position > x_cutoff[0] or x_position < x_cutoff[1]:
            continue
        for y in range(-y_repeat - 2 - y_offset, y_repeat + 1 - y_offset, 2):
            if x % 2 == 0:
                y_position = center_y + y_distance * y
            else:
                y_position = center_y + y_distance * (y + 1)
            if y_position > y_cutoff[0] or y_position < y_cutoff[1]:
                continue
            draw_background_hexagon(x_position, y_position, hexagon_radius)

    pygame.display.set_caption(f'{clock.get_fps() :.1f}')
    pygame.display.update()