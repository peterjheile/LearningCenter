import random
import pygame
pygame.init()
class Creature:
    def __init__(self):
        self.length,self.width = random(2,10)
        self.health = self.length * self.width
        self.xLocation = random (-, )
        self.yLocation = 

    def getCreatureHealth(self):
        return self.health

    def drawCreature(self):
        pygame.draw.rect(display, (0, 0 ,0), (self.x,self.y,self.width,self.height))
        
