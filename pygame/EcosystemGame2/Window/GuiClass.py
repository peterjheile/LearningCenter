from Window.ButtonClass import StartButton
from Window.ButtonClass import PauseButton

class GUI:
    def __init__(self):
        self.startButton = StartButton()
        self.pauseButton = PauseButton()
        self.buttons = [self.startButton,self.pauseButton]

    def draw(self,display):
        for i in self.buttons:
            i.draw(display)

    def update(self,mousePos,window):
        self.pauseButton.checkClicked(mousePos,self.startButton,window)

    


