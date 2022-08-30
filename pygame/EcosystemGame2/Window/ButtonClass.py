import pygame

class Button:
    def __init__(self):
        self.width = 200
        self.height = 100
        self.color = (221,160,221)

    def draw(self,display):
        pygame.draw.rect(display, self.color, (self.x,self.y,self.width,self.height))

class StartButton(Button):
    def __init__(self):
        super().__init__()
        self.x = 5
        self.y = 0
        self.tick = 60

    def checkClicked(self,clickPos):
        if (clickPos[0]>self.x and clickPos[0]<self.x+self.width) and (clickPos[1]>self.y and clickPos[1]<self.y+self.height):
            return True
        return False

class PauseButton(Button):
    def __init__(self):
        super().__init__()
        self.x = 5
        self.y = 105
        self.tick = 1

    def checkClicked(self,clickPos):
        if (clickPos[0]>self.x and clickPos[0]<self.x+self.width) and (clickPos[1]>self.y and clickPos[1]<self.y+self.height):
            return True
        return False



    