import pygame
from random import randint
import sys
sys.path.append("C:\\Users\\peter\\OneDrive\\Documents\\Peter Heile GitHub\\LearningCenter")
from NueralNetworks.EfficientNueralNet.BrainClass import Brain

class Creature:
    def __init__(self,xRange,yRange,mapX,mapY,zoom):
        self.width = 10*zoom
        self.height = self.width
        self.color = (255,255,0)
        self.x = randint(int(mapX),int(mapX+ (xRange - self.width)))
        self.y = randint(int(mapY),int(mapY+(yRange - self.height)))
        self.brain = Brain([9,15,20,10,2])
        self.energy = 500
        self.foodEaten = 0

    def draw(self,display):
        pygame.draw.rect(display, self.color, (self.x,self.y,self.width,self.height))

