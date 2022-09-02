import pygame
from random import randint
import sys
sys.path.append("C:\\Users\\peter\\OneDrive\\Documents\\Peter Heile GitHub\\LearningCenter")
from NueralNetworks.NueralNetRefurbished.AllClasses.BrainClass import Brain

class Creature:
    def __init__(self,xRange,yRange):
        self.width = randint(5,10)
        self.height = self.width
        self.color = (255,255,0)
        self.x = randint(0,xRange - self.width)
        self.y = randint(0,yRange - self.height)
        self.brain = Brain([6,10,10,2],[1,1,1,1,1,1])

    def draw(self,display):
        pygame.draw.rect(display, self.color, (self.x,self.y,self.width,self.height))

