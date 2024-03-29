import pygame
import sys
import pickle
from Window.WindowClass import Interactions

class Button:
    def __init__(self, text = ""):
        self.width = 200
        self.height = 100
        self.color = (221,160,221)
        self.text = text

    def draw(self,display):
        pygame.draw.rect(display, self.color, (self.x,self.y,self.width,self.height))
        self.showText(display)

    def showText(self,display):
        font = pygame.font.SysFont(None, 25)
        img = font.render(self.text, True, (0,0,255))
        display.blit(img, (self.x+10,self.y+30))

    def checkClicked(self, clickPos):
        if (clickPos[0]>self.x and clickPos[0]<self.x+self.width) and (clickPos[1]>self.y and clickPos[1]<self.y+self.height):
            return True
        return False


class StartButton(Button):
    def __init__(self, text):
        super().__init__(text)
        self.x = 5
        self.y = 0
        self.tick = 60

    def checkClicked(self,clickPos, parent = False):
        if parent:
            return super().checkClicked(clickPos)
        if (clickPos[0]>self.x and clickPos[0]<self.x+self.width) and (clickPos[1]>self.y and clickPos[1]<self.y+self.height):
            return True
        return False

class PauseButton(Button):
    def __init__(self, text):
        super().__init__(text)
        self.x = 5
        self.y = 105

    def checkClicked(self,clickPos,buttons,display,window, parent = False):
        if parent:
            return super().checkClicked(clickPos)
        else: 
            if (clickPos[0]>self.x and clickPos[0]<self.x+self.width) and (clickPos[1]>self.y and clickPos[1]<self.y+self.height):
                self.pause(buttons,display,window)
                    
    def pause(self,buttons,display,window):
        clock = pygame.time.Clock()
        continues = True
        while continues:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    if buttons[0].checkClicked(pygame.mouse.get_pos()):
                        continues = False
                    buttons[2].checkClicked(pygame.mouse.get_pos(),window)
                    buttons[3].checkClicked(pygame.mouse.get_pos(),window,display)
                    buttons[4].checkClicked(pygame.mouse.get_pos(),window,display)
                    buttons[5].checkClicked(pygame.mouse.get_pos(),window,display)


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
    def __init__(self,text):
        super().__init__(text)
        self.x = 5
        self.y = 210

    def checkClicked(self,clickPos,window, parent = False):
        if parent:
            return super().checkClicked(clickPos)
        if (clickPos[0]>self.x and clickPos[0]<self.x+self.width) and (clickPos[1]>self.y and clickPos[1]<self.y+self.height):
            self.save(window)

    def save(self,window):
        with open("EcoOutputData","wb") as file:
            pickle.dump(window,file)

class ZoomOutButton(Button):
    def __init__(self,text):
        super().__init__(text)
        self.x = 5
        self.y = 420
        
    def checkClicked(self,clickPos,window,display, parent = False):
        if parent:
            return super().checkClicked(clickPos)
        if (clickPos[0]>self.x and clickPos[0]<self.x+self.width) and (clickPos[1]>self.y and clickPos[1]<self.y+self.height):
            self.zoomOut(window,display)

    def zoomOut(self,window,display):
        window.updateDisplay([0,0],display,True,-1)

class ZoomInButton(Button):
    def __init__(self,text):
        super().__init__(text)
        self.x = 5
        self.y = 315
        
    def checkClicked(self,clickPos,window,display, parent = False):
        if parent:
            return super().checkClicked(clickPos)
        if (clickPos[0]>self.x and clickPos[0]<self.x+self.width) and (clickPos[1]>self.y and clickPos[1]<self.y+self.height):
            self.zoomIn(window,display)

    def zoomIn(self,window,display):
        window.updateDisplay([0,0],display,True,1)

class ReproduceButton(Button):
    def __init__(self,text):
        super().__init__(text)
        self.x = 5
        self.y = 525

    def checkClicked(self,clickPos,window, parent = False):
        if parent:
            return super().checkClicked(clickPos)
        if (clickPos[0]>self.x and clickPos[0]<self.x+self.width) and (clickPos[1]>self.y and clickPos[1]<self.y+self.height):
            self.reproduce(window.map)
        
    def reproduce(self, map):
        toLearn = len(map.allCreatures)-1
        Interactions.reproduce(map)
        Interactions.creaturesLearn(map,toLearn)

class ChangeLayoutButton(Button):
    def __init__(self,text):
        super().__init__(text)
        self.x = 5
        self.y = 630

    def checkClicked(self,clickPos,buttons,display,window, stopEdit = False):
        if not(stopEdit):
            if (clickPos[0]>self.x and clickPos[0]<self.x+self.width) and (clickPos[1]>self.y and clickPos[1]<self.y+self.height):
                self.editLayout(buttons,window,display)
        return super().checkClicked(clickPos)

    def editLayout(self,buttons,window,display):

        def editCoords(button, display):
            clock = pygame.time.Clock()
            continues = True
            while continues:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONUP:
                        continues = False
                        break
                    coords = pygame.mouse.get_pos()
                    # locationX, locationY = coords[0]-button.x,coords[1] - button.y
                    button.x = coords[0]
                    button.y = coords[1]

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

                    window.updateDisplay(movement,display,True)
                    clock.tick(60)

        clock = pygame.time.Clock()
        continues = True
        while continues:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if buttons[6].checkClicked(pygame.mouse.get_pos(), buttons, display, window, True):
                        continues = False
                        break
                    if buttons[0].checkClicked(pygame.mouse.get_pos(), True):
                        diffX,diffY = pygame.mouse.get_pos()[0] - buttons[0].x, pygame.mouse.get_pos()[1] - buttons[1].y
                        editCoords(buttons[0], display)
                    elif buttons[1].checkClicked(pygame.mouse.get_pos(),buttons,display,window, True):
                        diffX,diffY = pygame.mouse.get_pos()[0] - buttons[0].x, pygame.mouse.get_pos()[1] - buttons[1].y
                        editCoords(buttons[1], display)
                    elif buttons[2].checkClicked(pygame.mouse.get_pos(),window, True):
                        diffX,diffY = pygame.mouse.get_pos()[0] - buttons[0].x, pygame.mouse.get_pos()[1] - buttons[1].y
                        editCoords(buttons[2], display)
                    elif buttons[3].checkClicked(pygame.mouse.get_pos(),window,display, True):
                        diffX,diffY = pygame.mouse.get_pos()[0] - buttons[0].x, pygame.mouse.get_pos()[1] - buttons[1].y
                        editCoords(buttons[3], display)
                    elif buttons[4].checkClicked(pygame.mouse.get_pos(),window,display, True):
                        diffX,diffY = pygame.mouse.get_pos()[0] - buttons[0].x, pygame.mouse.get_pos()[1] - buttons[1].y
                        editCoords(buttons[4], display)
                    elif buttons[5].checkClicked(pygame.mouse.get_pos(),window, True):
                        diffX,diffY = pygame.mouse.get_pos()[0] - buttons[0].x, pygame.mouse.get_pos()[1] - buttons[1].y
                        editCoords(buttons[5], display)

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

            window.updateDisplay(movement,display,True)
            clock.tick(60)

    

    



    