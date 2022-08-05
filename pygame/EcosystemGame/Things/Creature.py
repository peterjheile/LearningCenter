from Things.Thing import Thing
class Creature(Thing):
    def __init__(self):
        super().__init__()
        self.color = (200,200,0)
        self.health = self.width*self.height

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


    

