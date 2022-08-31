from Window.ButtonClass import StartButton
from Window.ButtonClass import PauseButton
from Window.ButtonClass import SaveButton

class GUI:
    def __init__(self):
        self.startButton = StartButton()
        self.pauseButton = PauseButton()
        self.saveButton = SaveButton()
        self.buttons = [self.startButton,self.pauseButton,self.saveButton]

    def draw(self,display):
        for i in self.buttons:
            i.draw(display)

    def update(self,mousePos,display,window):
        self.pauseButton.checkClicked(mousePos,self.startButton,self.saveButton,display,window)
        self.saveButton.checkClicked(mousePos,window)
        

    


