import pygame
from random import randint

class Food:
    def __init__(self, xRange,yRange, mapX,mapY,zoom):
        self.width = 10*zoom
        self.height = 10*zoom
        self.x = randint(int(mapX),int(mapX+ (xRange - self.width)))
        self.y = randint(int(mapY),int(mapY+(yRange - self.height)))
        self.color = (0,0,255)
        self.energy = 1000

    def draw(self,display):
        pygame.draw.rect(display, self.color, (self.x,self.y,self.width,self.height))
