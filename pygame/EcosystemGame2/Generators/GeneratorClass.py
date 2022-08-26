from random import randint
import sys 
sys.path.append("AllObstacles")
from AllObstacles.ObstacleClass import Obstacle


class Generator:
    @classmethod
    def generateAllObstacle(self,xRange,yRange):
        return [Obstacle(xRange,yRange) for i in range(randint(10,20))]
