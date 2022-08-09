from Things.Obstacle import Obstacle
from Things.Creature import Creature
import pygame
import sys
from random import randint
from turtle import speed, width

class worldGen:
    def __init__(self,i1,i2):
        self.display = pygame.display.set_mode((800,600))
        self.display.fill((0,100,0))
        #in order of left, right, top, bottom
        self.allObstacles = []
        self.allCreatures = []
        self.map = Obstacle(((0,100,0)),0,0,randint(500,1000),randint(500,1000))
        # self.map = Obstacle(((0,100,0)),0,0,i1,i2)
        for i in range(randint(5,15)):
            self.createObstacle()
        for i in range(randint(5,15)):
            self.createCreature()

    def createObstacle(self):
        color = (randint(0,255),0,randint(0,255))
        x,y = randint(0,self.map.getWidth()),randint(0,self.map.getHeight())
        width,height = 10,10
        obstacle = Obstacle(color,x,y,width,height)
        self.allObstacles.append(obstacle)

    def createCreature(self):
        color = (randint(0,255),0,randint(0,255))
        x,y = randint(0,self.map.getWidth()),randint(0,self.map.getHeight())
        width,height = 10,10
        creature = Creature(color,x,y,width,height)
        self.allCreatures.append(creature)

    def moveAllCreatures(self):
        for i in self.allCreatures:
            factors = i.getMoveFactors()
            i.move(self.map, factors)

    def getAllCreatures(self):
        return self.allCreatures

    def getAllObstacles(self):
        return self.allObstacles

    def darwanism(self):
        for i in self.allCreatures:
            for x in self.allObstacles:
                #i.status returns false if they are not in the same location
                if (i.status(x)):
                    self.allCreatures.remove(i)

    def getMoveFactors(self):
        return [0,0]

    def updateWorld(self):
        self.display.fill((255,0,0))

        pygame.draw.rect(self.display,self.map.getColor(), (self.map.getX(),self.map.getY(),
        self.map.getWidth(),self.map.getHeight()))

        for i in self.allObstacles:
            pygame.draw.rect(self.display, i.getColor(), (i.getX(),i.getY(),i.getWidth(),i.getHeight()))
        for i in self.allCreatures:
            pygame.draw.rect(self.display, i.getColor(), (i.getX(),i.getY(),i.getWidth(),i.getHeight()))

        self.darwanism()

        pygame.display.update()


    

        
