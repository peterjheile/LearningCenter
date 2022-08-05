from random import randint
class Thing:
    def __init__(self, width = 10, height = 10):
        self.color = (randint(0,255),0,randint(0,255))
        self.x = randint(-500,500)
        self.y = randint(-500,500)
        self.width = width
        self.height = height

        # (color,x,y,width,height)
