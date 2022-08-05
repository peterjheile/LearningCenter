from random import randint
class Thing:
    def __init__(self,color,x,y,width,height):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # (color,x,y,width,height)
    #     ,color =(randint(0,255),0,randint(0,255)),x = randint(-500,500),y =randint(-500,500),
    # width = 10,height = 10
