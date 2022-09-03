from random import randint
import sys 
sys.path.append("AllObstacles")
sys.path.append("AllCreatures")
from AllObstacles.ObstacleClass import Obstacle
from AllCreatures.CreatureClass import Creature
from AllObstacles.FoodClass import Food



class Generator:
    
    @classmethod
    def generateAllObstacle(self,xRange,yRange):
        return [Obstacle(xRange,yRange) for i in range(randint(50,100))]

    @classmethod
    def generateAllCreatures(self,xRange,yRange):
        return [Creature(xRange,yRange) for i in range(randint(50,100))]

    @classmethod
    def generateAllFood(self,xRange,yRange):
        return [Food(xRange,yRange) for i in range(randint(50,100))]
