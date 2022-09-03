import pygame
from random import randint

class Food:
    def __init__(self, xRange,yRange):
        self.width = 10
        self.height = 10
        self.x = randint(0,xRange - self.width)
        self.y = randint(0,yRange - self.height)
        self.color = (0,0,255)
        self.energy = self.width * self.height

    def draw(self,display):
        pygame.draw.rect(display, self.color, (self.x,self.y,self.width,self.height))
