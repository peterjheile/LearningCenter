import pygame
from random import randint

class Creature:
    def __init__(self,xRange,yRange):
        self.width = randint(5,10)
        self.height = self.width
        self.color = (200,0,0)
        self.x = randint(0,xRange - self.width)
        self.y = randint(0,yRange - self.height)

    def draw(self,display):
        pygame.draw.rect(display, self.color, (self.x,self.y,self.width,self.height))
