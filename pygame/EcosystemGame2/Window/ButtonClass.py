import pygame
import sys
import pickle

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

    def checkClicked(self,clickPos,startButton,saveButton,display,window):
        if (clickPos[0]>self.x and clickPos[0]<self.x+self.width) and (clickPos[1]>self.y and clickPos[1]<self.y+self.height):
            self.pause(startButton,saveButton,display,window)
                    
    def pause(self,startButton,saveButton,display,window):
        clock = pygame.time.Clock()
        continues = True
        while continues:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    if startButton.checkClicked(pygame.mouse.get_pos()):
                        continues = False
                    saveButton.save(window)

            keys = pygame.key.get_pressed()
            movement = [0,0]
            if keys[pygame.K_a]:
                movement[0] +=5
            if keys[pygame.K_d]:
                movement[0] -=5
            if keys[pygame.K_w]:
                movement[1] +=5
            if keys[pygame.K_s]:
                movement[1] -=5
            window.updateDisplay(movement,display,False)
            clock.tick(60)

class SaveButton(Button):
    def __init__(self):
        super().__init__()
        self.x = 5
        self.y = 210
        self.tick = 1

    def checkClicked(self,clickPos,window):
        if (clickPos[0]>self.x and clickPos[0]<self.x+self.width) and (clickPos[1]>self.y and clickPos[1]<self.y+self.height):
            self.save(window)

    def save(self,window):
        with open("EcoOutputData","wb") as file:
            pickle.dump(window,file)
    



    