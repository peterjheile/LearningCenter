from Things.Obstacle import Obstacle
from Things.Creature import Creature
import pygame
import sys
from random import randint
from turtle import speed, width

class worldGen:
    def __init__(self):
        self.display = pygame.display.set_mode((800,600))
        self.display.fill((0,100,0))
        self.mapLength = randint(1000,2000)
        self.mapHeight = randint(1000,2000)
        self.mapBorders = [0,self.mapLength,0,(-1*self.mapHeight)]
        self.allObstacles = []
        self.allCreatures = []

        self.borders = self.createBorders()
        for i in range(randint(5,15)):
            self.createObstacle()
        for i in range(randint(5,15)):
            self.createCreature()

    def createObstacle(self):
        color = (randint(0,255),0,randint(0,255))
        x,y = randint(0,self.mapLength),randint(0,self.mapHeight)
        width,height = 10,10
        obstacle = Obstacle(color,x,y,width,height)
        self.allObstacles.append(obstacle)

    def createCreature(self):
        color = (randint(0,255),0,randint(0,255))
        x,y = randint(0,self.mapLength),randint(0,self.mapHeight)
        width,height = 10,10
        creature = Creature(color,x,y,width,height)
        self.allCreatures.append(creature)

    def createBorders(self):
        obstacle = Obstacle((0,100,0),0,0,self.mapLength,self.mapHeight)
        self.allObstacles.append(obstacle)
    
    # def createBorders(self):
    #     xBorders = []
    #     yBorders = []
    #     self.Obstacle((255,0,0),randint(-1000,-5000),randint(-1000,-5000),)
    #     self.

    def moveAllCreatures(self, movement = [0,0]):
        for i in self.allCreatures:
            i.setX(i.getX() + movement[0] + randint(-3,3))
            i.setY(i.getY() + movement[1] + randint(-3,3))

    def moveAllObstacles(self, movement):
        for i in self.allObstacles:
            i.setX(i.getX() + movement[0])
            i.setY(i.getY() + movement[1])

    def getAllCreatures(self):
        return self.allCreatures

    def getAllObstacles(self):
        return self.allObstacles

    def updateWorld(self):
        self.display.fill((255,0,0))
        for i in self.allObstacles:
            pygame.draw.rect(self.display, i.getColor(), (i.getX(),i.getY(),i.getWidth(),i.getHeight()))
        for i in self.allCreatures:
            pygame.draw.rect(self.display, i.getColor(), (i.getX(),i.getY(),i.getWidth(),i.getHeight()))
        pygame.display.update()

    

        
