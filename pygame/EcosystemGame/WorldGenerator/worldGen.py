from Things.Obstacle import Obstacle
from Things.Creature import Creature
import pygame
import sys
from random import randint
from turtle import speed, width
import math

class worldGen:
    def __init__(self,i1 = 0,i2 = 0):
        self.display = pygame.display.set_mode((1200,700))
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
            factors = self.getMoveFactors(i)
            i.move(self.map, factors)
        self.darwanism()

    def getAllCreatures(self):
        return self.allCreatures

    def getAllObstacles(self):
        return self.allObstacles

    def darwanism(self):
        i = 0
        totalCreatures = len(self.allCreatures) - 1
        while i < totalCreatures:
            for x in self.allObstacles:
                #i.status returns false if they are not in the same location
                if (self.allCreatures[i].status(x,self.map)):
                    self.allCreatures.pop(i)
                    totalCreatures -=1
                    print("Creature Died")
            i += 1

    # def getClosest(self,creature):
    #     closest = 100000
    #     for i in self.allObstacles:
    #         distance = math.dist((i.x,i.y),(creature.x,creature.y))
    #         if distance < closest:
    #             closest = distance
    #     return distance
            
    def getMoveFactors(self,creature):

        closest,obstacle = 100000, self.allCreatures[0]
        for i in self.allObstacles:
            distance = math.dist((i.x,i.y),(creature.x,creature.y))
            if distance < closest:
                closest,obstacle = distance,i
        closest = closest/self.map.height
        
        
        #finds angle of closest creature
        xDist = (i.x - creature.x) if (i.x - creature.x != 0) else 1
        yDist = (i.y - creature.y)
        angle = math.degrees((math.atan(abs(yDist)/abs(xDist))))
        if (xDist < 0 and yDist > 0):
            angle = angle+90
        elif (xDist < 0 and yDist < 0):
            angle = angle + 180
        elif (xDist > 0 and yDist < 0):
            angle = angle + 270
        angle = angle/360

        # print([distance,angle])
        return [closest,angle]

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


    

        
