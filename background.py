# background.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
import pygame, random
from variables import *

colorMin = 0
colorMax = 195
colorDiff = 60
hexGradiant = 11

backHexagon = (random.randint(colorMin, colorMax), random.randint(colorMin, colorMax), random.randint(colorMin, colorMax))
frontHexagon = (backHexagon[0] + colorDiff, backHexagon[1] + colorDiff, backHexagon[2] + colorDiff)

def draw_foreground_hexagon(x, y, hexagon_radius, color):
    straight_x = hexagon_radius * (4 / 5)
    corner_x = straight_x / 2
    corner_y = straight_x * (3 ** (1/2) / 2)
    pygame.draw.polygon(screen, color, ((x + corner_x, y + corner_y), (x + straight_x, y), (x + corner_x, y - corner_y), (x - corner_x, y - corner_y), (x - straight_x, y), (x - corner_x, y + corner_y)))

def draw_background_hexagon(x, y, hexagon_radius, color):
    straight_x = hexagon_radius
    corner_x = straight_x / 2
    corner_y = straight_x * (3 ** (1/2) / 2)
    pygame.draw.polygon(screen, color, ((x + corner_x, y + corner_y), (x + straight_x, y), (x + corner_x, y - corner_y), (x - corner_x, y - corner_y), (x - straight_x, y), (x - corner_x, y + corner_y)))

def draw_hexagon(x, y, hexagonRadius, cameraPosition, cameraPerspective):
    center_x = round(SCREEN_WIDTH / 2)
    center_y = round(SCREEN_HEIGHT / 2)
    true_x = x - center_x - cameraPosition[0] * cameraPerspective
    true_y = y - center_y - cameraPosition[1] * cameraPerspective
    distanceAway = (true_x ** 2 + true_y ** 2) ** (1/2)

    offsetColor = round(distanceAway / (hexagonRadius * hexGradiant))
    placeHolder = [backHexagon[0] - offsetColor, backHexagon[1] - offsetColor, backHexagon[2] - offsetColor]
    if placeHolder[0] < colorMin:
        placeHolder[0] = colorMin
    if placeHolder[1] < colorMin:
        placeHolder[1] = colorMin
    if placeHolder[2]  < colorMin:
        placeHolder[2] = colorMin
    backColor = (placeHolder[0], placeHolder[1], placeHolder[2])
    placeHolder = [frontHexagon[0] - offsetColor, frontHexagon[1] - offsetColor, frontHexagon[2] - offsetColor]
    if placeHolder[0] < colorDiff:
        placeHolder[0] = colorDiff
    if placeHolder[1] < colorDiff:
        placeHolder[1] = colorDiff
    if placeHolder[2] < colorDiff:
        placeHolder[2] = colorDiff
    frontColor = (placeHolder[0], placeHolder[1], placeHolder[2])

    draw_background_hexagon(x, y, hexagonRadius, backColor)
    draw_foreground_hexagon(x, y, hexagonRadius, frontColor)

def draw_background(cameraPosition, cameraPerspective):
    center_x = round(SCREEN_WIDTH / 2) + cameraPosition[0]
    center_y = round(SCREEN_HEIGHT / 2) + cameraPosition[1]

    # Define the Radius of the hexagon
    hexagon_radius = SCREEN_WIDTH / 32 / cameraPerspective
    # Calculates the distance between hexagons
    x_distance = hexagon_radius * (3 / 2)
    y_distance = hexagon_radius * (3 ** (1/2) / 2)
    # Calculates the cutoff distance of hexagons
    x_cutoff = [-x_distance, SCREEN_WIDTH + x_distance]
    y_cutoff = [-y_distance, SCREEN_HEIGHT + y_distance]

    x_offset = round(cameraPosition[0] / x_distance)
    y_offset = round(cameraPosition[1] / y_distance)
    if y_offset % 2 != 0:
        y_offset += 1
    x_repeat = round(SCREEN_WIDTH / x_distance)
    y_repeat = round(SCREEN_HEIGHT / y_distance)
    if y_repeat % 2 != 0:
        y_repeat += 1

    #print(cameraPosition[0] * cameraPerspective, cameraPosition[1] * cameraPerspective)

    screen.fill(White)

    for x in range(-x_repeat - x_offset, x_repeat + 1 - x_offset):
        x_position = center_x + x_distance * x
        if x_position > x_cutoff[1] or x_position < x_cutoff[0]:
            continue
        for y in range(-y_repeat - 2 - y_offset, y_repeat + 1 - y_offset, 2):
            if x % 2 == 0:
                y_position = center_y + y_distance * y
            else:
                y_position = center_y + y_distance * (y + 1)
            if y_position > y_cutoff[1] or y_position < y_cutoff[0]:
                continue
            draw_hexagon(x_position, y_position, hexagon_radius, cameraPosition, cameraPerspective)

    pygame.display.set_caption(f'{clock.get_fps() :.1f}')
    pygame.display.update()