import pygame
import sys
sys.path.append("AllObstacles")
sys.path.append("Generators")
sys.path.append("AllCreatures")
from AllObstacles.ObstacleClass import Obstacle
from Generators.GeneratorClass import Generator
from AllCreatures.CreatureClass import Creature

class Map:
    def __init__(self,width = 800, height = 650):
        self.width = 3000
        self.height = 3000
        self.x = 0
        self.y = 0
        self.color = (0,100,0)
        self.allObstacles = Generator.generateAllObstacle(self.width,self.height)
        self.allCreatures = Generator.generateAllCreatures(self.width,self.height)
        self.allFood = Generator.generateAllFood(self.width,self.height)
        self.zoom = 1
        self.allow = True

    def drawMap(self,display):
        pygame.draw.rect(display, self.color, (self.x,self.y,self.width,self.height))

    def drawAllObstacles(self,display):
        for i in self.allObstacles:
            i.draw(display)

    def drawAllCreatures(self,display):
        for i in self.allCreatures:
            i.draw(display)

    def drawAllFood(self, display):
        for i in self.allFood:
            i.draw(display)

    def draw(self,display):
        self.drawMap(display)
        self.drawAllObstacles(display)
        self.drawAllCreatures(display)
        self.drawAllFood(display)

    

