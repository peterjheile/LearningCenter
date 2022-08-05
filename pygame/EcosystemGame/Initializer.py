from turtle import speed, width
import pygame
import sys
import math
from WorldGenerator.worldGen import worldGen
from UserInteractions.MoveScreen import Interactions

pygame.init()
world = worldGen()
clock = pygame.time.Clock()


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()

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
    

    Interactions.moveScreen(world, movement)
    print(movement)
    # world.moveAllCreatures()
    world.updateWorld()
    clock.tick(60)
    




    
