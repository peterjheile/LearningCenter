from random import randint
class Thing:
    def __init__(self):
        self.color = (randint(0,255),0,randint(0,255))
        self.x = randint(-500,500)
        self.y = randint(-500,500)
        self.width = 10
        self.height = 10

        # (color,x,y,width,height)
