# main.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
# If pygame is not installed: sudo apt install python3-pygame
# To run: python3 Racing-Game/main.py
import pygame
from variables import *
from background import draw_background

def main():
	run = True
	screenGrab = False
	newmousePosition = (0, 0)
	oldmousePosition = (0, 0)
	
	cameraPerspective = 1
	perspectiveChange = 1.2
	cameraPosition = [0, 0]
	cameraVelocity = [0, 0]
	cameraFriction = .9
	centerCamera = False
	centerSpeed = .9

	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					screenGrab = True
					centerCamera = False
			if event.type == pygame.MOUSEWHEEL:
				if event.y == -1:
					if cameraPerspective < 2:
						cameraPerspective *= perspectiveChange
						cameraPosition[0] /= perspectiveChange
						cameraPosition[1] /= perspectiveChange
				if event.y == 1:
					if cameraPerspective > .5:
						cameraPerspective /= perspectiveChange
						cameraPosition[0] *= perspectiveChange
						cameraPosition[1] *= perspectiveChange
			if event.type == pygame.MOUSEBUTTONUP:
				if event.button == 1:
					if screenGrab == True:
						screenGrab = False
						cameraVelocity[0] += newmousePosition[0] - oldmousePosition[0]
						cameraVelocity[1] += newmousePosition[1] - oldmousePosition[1]
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					run = False
				if event.key == pygame.K_c:
					if screenGrab == False:
						centerCamera = True
			if event.type == pygame.QUIT:
				run = False
		
		oldmousePosition = newmousePosition
		newmousePosition = pygame.mouse.get_pos()
		if newmousePosition[0] > 0 and newmousePosition[0] < SCREEN_WIDTH and newmousePosition[1] > 0 and newmousePosition[1] < SCREEN_HEIGHT:
			if screenGrab == True:
				cameraPosition[0] += newmousePosition[0] - oldmousePosition[0]
				cameraPosition[1] += newmousePosition[1] - oldmousePosition[1]
		else:
			if screenGrab == True:
				screenGrab = False
				cameraVelocity[0] += newmousePosition[0] - oldmousePosition[0]
				cameraVelocity[1] += newmousePosition[1] - oldmousePosition[1]
		if centerCamera == False:
			if screenGrab == False:
				cameraPosition[0] += cameraVelocity[0]
				cameraPosition[1] += cameraVelocity[1]
				cameraVelocity[0] *= cameraFriction
				cameraVelocity[1] *= cameraFriction
		else:
			cameraPosition[0] *= centerSpeed
			cameraPosition[1] *= centerSpeed
		draw_background(cameraPosition, cameraPerspective)
	pygame.quit()
main()
