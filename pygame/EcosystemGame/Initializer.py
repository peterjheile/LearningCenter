from turtle import speed, width
import pygame
import sys
import math
from WorldGenerator.worldGen import worldGen

pygame.init()
world = worldGen()
clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()

    keys = pygame.key.get_pressed()

    world.moveAllCreatures()
    world.updateWorld()
    clock.tick(60)
    




    
