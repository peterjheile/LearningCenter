import pygame
import sys
sys.path.append("AllObstacles")
sys.path.append("Generators")
from AllObstacles.ObstacleClass import Obstacle
from Generators.GeneratorClass import Generator

class Map:
    def __init__(self,width = 800, height = 650):
        self.width = 800
        self.height = 650
        self.x = 0
        self.y = 0
        self.color = (0,100,0)
        self.allObstacles = Generator.generateAllObstacle(self.width,self.height)

    def drawMap(self,display):
        pygame.draw.rect(display, self.color, (self.x,self.y,self.width,self.height))

    def drawAllObstacles(self,display):
        for i in self.allObstacles:
            pygame.draw.rect(display,i.color,(i.x,i.y,i.width,i.height))

    def draw(self,display):
        self.drawMap(display)
        self.drawAllObstacles(display)

    

