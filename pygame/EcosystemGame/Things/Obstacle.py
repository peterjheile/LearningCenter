from Things.Thing import Thing
class Obstacle(Thing):
    def __init__(self,color,x,y,width,height):
        super().__init__(color,x,y,width ,height)

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

        



