from Window.ButtonClass import StartButton
from Window.ButtonClass import PauseButton
from Window.ButtonClass import SaveButton
from Window.ButtonClass import ZoomInButton
from Window.ButtonClass import ZoomOutButton
from Window.ButtonClass import ReproduceButton

class GUI:
    def __init__(self):
        self.startButton = StartButton("Start")
        self.pauseButton = PauseButton("Pause")
        self.saveButton = SaveButton("Save")
        self.ZoomInButton = ZoomInButton("Zoom In")
        self.ZoomOutButton = ZoomOutButton("Zoom out")
        self.reproduceButton = ReproduceButton("Reproduce")
        self.buttons = [self.startButton,self.pauseButton,self.saveButton,self.ZoomInButton,self.ZoomOutButton,self.reproduceButton]

    def draw(self,display):
        for i in self.buttons:
            i.draw(display)

    def update(self,mousePos,display,window):
        self.pauseButton.checkClicked(mousePos,self.buttons,display,window)
        self.saveButton.checkClicked(mousePos,window)
        self.ZoomInButton.checkClicked(mousePos,window,display)
        self.ZoomOutButton.checkClicked(mousePos,window,display)
        self.reproduceButton.checkClicked(mousePos,window)

        

    


