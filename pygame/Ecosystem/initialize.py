from turtle import speed, width
import pygame
import sys
import math
from CreatureGen.Creatures import Creatures
from Environment.Display import Background

pygame.init()

display = pygame.display.set_mode((800,600))
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
player_move = [400,300]


background = Background()


while True:
    
    display.fill(background.get_background_color())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()

    keys = pygame.key.get_pressed()

    borders = background.get_border_locations()

    pygame.draw.rect(display,(255,0,0), ((borders[0]-5000)-player_move[0]+400, (borders[2]-250)-player_move[1]+300, 5000,5000))
    pygame.draw.rect(display,(255,0,0), (borders[1]-player_move[0]+400, (borders[2]-250)-player_move[1]+300, 5000,5000))
    pygame.draw.rect(display,(255,0,0), ((borders[0]-250)-player_move[0]+400, (borders[2]-5000)-player_move[1]+300, 5000,5000))
    pygame.draw.rect(display,(255,0,0), ((borders[0]-250)-player_move[0]+400, borders[3]-player_move[1]+300, 5000,5000))


    pygame.draw.rect(display,(0,0,255), (0-player_move[0],0-player_move[1],100,100))

    # if keys[pygame.K_a]:
    #     player_move[0] -=5
    # if keys[pygame.K_d]:
    #     player_move[0] +=5
    # if keys[pygame.K_w]:
    #     player_move[1] -=5
    # if keys[pygame.K_s]:
    #     player_move[1] +=5

    if keys[pygame.K_a] and (player_move[0] > background.get_border_locations()[0]+5):
        player_move[0] -=5
    if keys[pygame.K_d] and (player_move[0] < background.get_border_locations()[1]-5):
        player_move[0] +=5
    if keys[pygame.K_w] and (player_move[1] > background.get_border_locations()[2]+5):
        player_move[1] -=5
    if keys[pygame.K_s] and (player_move[1] < background.get_border_locations()[3]+5):
        player_move[1] +=5

    # print(background.get_border_locations())
    # print(player_move)

    player.main(display)
    
    clock.tick(60)
    pygame.display.update()
    