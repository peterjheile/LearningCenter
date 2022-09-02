import pygame
import sys 
sys.path.append("Map")
from Maps.MapClass import Map
from Window.InteractionsClass import Interactions
from Window.GuiClass import GUI

class Window:
    def __init__ (self):
        self.length = 1200
        self.width = 700
        self.color = (255,0,0)
        # self.createDisplay()
        self.createMap()
        self.createGUI()

    # def createDisplay(self):
    #     self.display = pygame.display.set_mode((self.length,self.width))
    #     self.display.fill(self.color)

    def createMap(self):
        self.map = Map()

    def createGUI(self):
        self.gui = GUI()

    def updateDisplay(self, displacement,display,all = True,zoom = 0):
        Interactions.displaceScreen(self.map,self.map.allObstacles,self.map.allCreatures,displacement,all,zoom)
        Interactions.eliminateCreatures(self.map, self.map.allObstacles,self.map.allCreatures)
        Interactions.creaturesLearn(self.map)
        display.fill((255,0,0))
        self.map.draw(display)
        self.gui.draw(display)
        pygame.display.update()
