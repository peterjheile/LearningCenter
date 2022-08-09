from Things.Thing import Thing
from random import randint
from Things.NueralNetCreator.BrainClass import Brain



class Creature(Thing):
    def __init__(self,color,x,y,width,height):
        super().__init__(color,x,y,5,5)
        self.color = (255,255,0)
        self.health = self.width*self.height
        self.brain = Brain([3,4,2],[1,1,1])

    # def move(self,map,movement = 3):
    #     #in order of left, right, top, bottom
    #     # moveLeft = -movement if self.getX()-movement>map.getX() else 0
    #     # moveRight = movement if self.getX()+movement<map.getX()+map.getWidth() else 0
    #     # moveDown = movement if self.getY()+movement<map.getY()+map.getHeight() else 0
    #     # moveUp = -movement if self.getY()-movement>map.getY() else 0
    #     # self.x = self.x + randint(moveLeft,moveRight)
    #     # self.y = self.y + randint(moveUp,moveDown)
    

    def move(self,map,inputs):
        movements = self.brain.calculate(inputs)
        self.x = self.x + movements[0]
        self.y = self.y + movements[1]
        # print(movements[0], movements[1])

    def status(self, thing, map):
        if ((thing.x < self.x) and ((thing.x + thing.width) >= self.x)) and (thing.y < self.y) and ((thing.y + thing.height) >= self.x):
            return True
        elif ((thing.x < map.x) or (thing.x > (map.x + map.width))):
            return True
        elif ((thing.y < map.y) or (thing.y > (map.y + map.height))):
            return True
        return False


    def getHealth(self):
        return self.health

    def getColor(self):
        return self.color

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def setHealth(self,health):
        self.health = health

    def setColor(self,color):
        self.color = color

    def setX(self,x):
        self.x = x

    def setY(self,y):
        self.y = y

    def setWidth(self,width):
        self.width = width

    def setHeight(self,height):
        self.height = height


    

