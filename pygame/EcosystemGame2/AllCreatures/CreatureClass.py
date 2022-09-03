import pygame
from random import randint
import sys
sys.path.append("C:\\Users\\peter\\OneDrive\\Documents\\Peter Heile GitHub\\LearningCenter")
from NueralNetworks.NueralNetRefurbished.AllClasses.BrainClass import Brain

class Creature:
    def __init__(self,xRange,yRange,mapX,mapY,zoom):
        self.width = randint(5,10)*zoom
        self.height = self.width
        self.color = (255,255,0)
        self.x = randint(int(mapX),int(mapX+ (xRange - self.width)))
        self.y = randint(int(mapY),int(mapY+(yRange - self.height)))
        self.brain = Brain([9,12,12,2],[1,1,1,1,1,1,1,1,1])
        self.energy = 1000

    def draw(self,display):
        pygame.draw.rect(display, self.color, (self.x,self.y,self.width,self.height))

