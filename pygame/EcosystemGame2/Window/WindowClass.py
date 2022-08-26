import pygame
import sys 
sys.path.append("Map")
from Maps.MapClass import Map
from Window.InteractionsClass import Interactions

class Window:
    def __init__ (self):
        self.length = 1200
        self.width = 700
        self.color = (255,0,0)
        self.createDisplay()
        self.createMap()

    def createDisplay(self):
        self.display = pygame.display.set_mode((self.length,self.width))
        self.display.fill(self.color)

    def createMap(self):
        self.map = Map()

    def updateDisplay(self, displacement):
        Interactions.displaceScreen(self.map,self.map.allObstacles,displacement)
        self.display.fill(self.color)
        self.map.draw(self.display)
        pygame.display.update()
