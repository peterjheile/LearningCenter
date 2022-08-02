from turtle import speed, width
import pygame
import sys
import math
from Environment.Display import Background

pygame.init()

display = pygame.display.set_mode((900,600))
clock = pygame.time.Clock()

class Player:
    def __init__(self, x, y, width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def main(self, display):
        pygame.draw.rect(display, (0, 0 ,0), (self.x,self.y,self.width,self.height))

player = Player(400,300,16,16)
background = Background()
player_move = [0,0]


while True:
    
    display.fill(background.get_background_color())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.QUIT

    keys = pygame.key.get_pressed()


    pygame.draw.rect(display,(255,0,0), (100-player_move[0],100-player_move[1],32,32))

    if keys[pygame.K_a]:
        player_move[0] -=5
    if keys[pygame.K_d]:
        player_move[0] +=5
    if keys[pygame.K_w]:
        player_move[1] -=5
    if keys[pygame.K_s]:
        player_move[1] +=5

    player.main(display)
    
    clock.tick(60)
    pygame.display.update()