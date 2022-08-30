import pygame
import sys
import math
from Window.WindowClass import Window

pygame.init()

window = Window()
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            window.gui.update(pygame.mouse.get_pos(),window)

    keys = pygame.key.get_pressed()

    movement = [0,0]

    if keys[pygame.K_a]:
        movement[0] +=5
    if keys[pygame.K_d]:
        movement[0] -=5
    if keys[pygame.K_w]:
        movement[1] +=5
    if keys[pygame.K_s]:
        movement[1] -=5

    window.updateDisplay(movement)
    clock.tick(60)
