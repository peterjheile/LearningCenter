from Things.Obstacle import Obstacle
from Things.Creature import Creature
import pygame
import sys
from random import randint
from turtle import speed, width

class worldGen:
    def __init__(self):
        self.display = pygame.display.set_mode((800,600))
        self.display.fill((0,200,0))
        self.allObstacles = []
        self.allCreatures = []
        for i in range(randint(5,15)):
            self.createObstacle()
        for i in range(randint(5,15)):
            self.createCreature()

    def createObstacle(self):
        self.obstacle = Obstacle()
        self.allObstacles.append(self.obstacle)

    def createCreature(self):
        self.creature = Creature()
        self.allCreatures.append(self.creature)

    def moveAllCreatures(self):
        for i in self.allCreatures:
            i.setX(i.getX() + randint(-3,3))
            i.setY(i.getY() + randint(-3,3))

    def updateWorld(self):
        self.display.fill((0,100,0))
        for i in self.allObstacles:
            pygame.draw.rect(self.display, i.getColor(), (i.getX(),i.getY(),i.getWidth(),i.getHeight()))
        for i in self.allCreatures:
            pygame.draw.rect(self.display, i.getColor(), (i.getX(),i.getY(),i.getWidth(),i.getHeight()))

        pygame.display.update()

    

        
