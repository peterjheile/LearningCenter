from Window.ButtonClass import StartButton
from Window.ButtonClass import PauseButton

class GUI:
    def __init__(self):
        self.startButton = StartButton()
        self.pauseButton = PauseButton()
        self.buttons = [self.startButton,self.pauseButton]
        self.tick = 60

    def draw(self,display):
        for i in self.buttons:
            i.draw(display)

    def update(self,mousePos):
        self.updateTick(mousePos)

    def updateTick(self,mousePos):
        for i in self.buttons:
            if i.checkClicked(mousePos):
                self.tick = i.tick
                break
    


