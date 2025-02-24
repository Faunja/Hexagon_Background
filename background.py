# background.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
import pygame, random
from variables import *

hexagonMin = 0
hexagonMax = 195
hexagonDiff = 60
backHexagon = (random.randint(hexagonMin, hexagonMax), random.randint(hexagonMin, hexagonMax), random.randint(hexagonMin, hexagonMax))
frontHexagon = (backHexagon[0] + hexagonDiff, backHexagon[1] + hexagonDiff, backHexagon[2] + hexagonDiff)

def draw_hexagon(x, y, hexagon_radius, color):
	straight_x = hexagon_radius
	corner_x = straight_x / 2
	corner_y = straight_x * (3 ** (1/2) / 2)
	pygame.draw.polygon(screen, color, ((x + corner_x, y + corner_y), (x + straight_x, y), (x + corner_x, y - corner_y), (x - corner_x, y - corner_y), (x - straight_x, y), (x - corner_x, y + corner_y)))

def color_check(color, difference, colorMin):
	newColor = [color[0] - difference, color[1] - difference, color[2] - difference]
	if newColor[0] < colorMin:
		newColor[0] = colorMin
	if newColor[1] < colorMin:
		newColor[1] = colorMin
	if newColor[2]  < colorMin:
		newColor[2] = colorMin
	return newColor

def draw_background_hexagon(x, y, hexagonRadius, cameraPosition, cameraPerspective):
	center_x = round(SCREEN_WIDTH / 2)
	center_y = round(SCREEN_HEIGHT / 2)
	true_x = x - center_x - cameraPosition[0]
	true_y = y - center_y - cameraPosition[1]
	distanceAway = (true_x ** 2 + true_y ** 2) ** (1/2)
	hexGradiant = 4

	offsetColor = round(distanceAway / (hexagonRadius * hexGradiant))
	backColor = color_check(backHexagon, offsetColor, hexagonMin)
	frontColor = color_check(frontHexagon, offsetColor, hexagonMin + hexagonDiff)

	draw_hexagon(x, y, hexagonRadius, backColor)
	radiusDiff = 9 / 10
	draw_hexagon(x, y, hexagonRadius * radiusDiff, frontColor)

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
			draw_background_hexagon(x_position, y_position, hexagon_radius, cameraPosition, cameraPerspective)