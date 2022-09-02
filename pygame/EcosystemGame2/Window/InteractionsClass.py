from random import randint
import sys
import math
import pygame
sys.path.append("Map")
from Maps.MapClass import Map

class Interactions:
    @classmethod
    def displaceScreen(Interactions,map,obstacles,creatures,displacement, all,zoom = 0):
        Interactions.zoom(map,zoom)
        map.x += displacement[0]
        map.y += displacement[1]
        for i in obstacles:
            i.x += displacement[0]
            i.y += displacement[1]
        for i in creatures:
            movement = Interactions.creatureMove(i,map,obstacles)
            if all:
                i.x += displacement[0] + Interactions.adjustMovements(zoom,map,Interactions.tanh(movement[0]))
                i.y += displacement[1] + Interactions.adjustMovements(zoom,map,Interactions.tanh(movement[1]))
            else:
                i.x += displacement[0] 
                i.y += displacement[1]

    @classmethod
    def zoom(self,map,zoom = 0):
        if zoom == 1:
            map.width = map.width*1.2
            map.height = map.height*1.2
            map.x = map.x*1.2
            map.y = map.y*1.2
            for i in map.allObstacles:
                i.width = i.width*1.2
                i.height = i.height*1.2
                i.x = i.x*1.2
                i.y = i.y*1.2
            for i in map.allCreatures:
                i.width = i.width*1.2
                i.height = i.height*1.2
                i.x = i.x*1.2
                i.y = i.y*1.2

        elif (zoom == -1):
            map.width = map.width/1.2
            map.height = map.height/1.2
            map.x = map.x/1.2
            map.y = map.y/1.2
            for i in map.allObstacles:
                i.width = i.width/1.2
                i.height = i.height/1.2
                i.x = i.x/1.2
                i.y = i.y/1.2
            for i in map.allCreatures:
                i.width = i.width/1.2
                i.height = i.height/1.2
                i.x = i.x/1.2
                i.y = i.y/1.2
        
    @classmethod
    def adjustMovements(self,zoom,map,movement):
        if zoom == 0:
            map.allowed = True
        if map.allowed:
            if zoom == 1:
                # print(zoom)
                map.zoom = map.zoom*1.2
                map.allowed = False
            elif zoom ==-1:
                # print(zoom)
                map.zoom = map.zoom/1.2
                map.allowed = False
        return movement*map.zoom

    @classmethod
    def tanh(Interactions, num):
        if math.isnan(num):
            return 0
        else:
            return 1/(1+math.e**-num) - .5

    @classmethod
    def creatureMove(Interactions,i,map,obstacles):
        movement = Interactions.getMoveFactors(i,map,obstacles)
        return i.brain.calculate(movement)

    @classmethod
    def getMoveFactors(Interactions,cre,map,obstacles):
        #gets the closest obstacle and passes the distance as a move factor
        closest,obstacle = 100000,obstacles[0]
        for obs in obstacles:
            distance = math.dist((cre.x,cre.y),(obs.x,obs.y))
            if distance < closest:
                closest,obstacle = distance,obs
        closest = closest

        #distance to the corner of the map
        mapDistance = math.dist((cre.x,cre.y),(map.x,map.y))

        #finds angle of closest obstacle
        xDist = (obstacle.x - cre.x) if (obstacle.x - cre.x != 0) else 1
        yDist = (obstacle.y - cre.y)
        angle = math.degrees((math.atan(abs(yDist)/abs(xDist))))
        if (xDist < 0 and yDist > 0):
            angle = angle+90
        elif (xDist < 0 and yDist < 0):
            angle = angle + 180
        elif (xDist > 0 and yDist < 0):
            angle = angle + 270
        return [angle,closest, mapDistance]
        

    @classmethod
    def eliminateCreatures(Interactions, map,obstacles, creatures):
        def continues(cre,creatures,obstacles):
            for obs in obstacles:
                if Interactions.checkCollision(cre,obs):
                    creatures.remove(cre)
                    return 
            # Can be uncommented to add collisions between creatures for creature death
            for cre2 in creatures:
                if Interactions.checkCollision(cre,cre2) and (cre!=cre2):
                    creatures.remove(cre)
                    creatures.remove(cre2)
                    return

        for cre in creatures:
            if Interactions.checkCollision(cre,map):
                creatures.remove(cre)
                continue
            continues(cre,creatures,obstacles)
            
        
    @classmethod
    def checkCollision(Interactions, o1, o2):
        #used to check collision between two things in the
        if isinstance(o2,Map):
            return ((o1.x+o1.width>o2.x+o2.width) or (o1.x<o2.x) or (o1.y+o1.height>o2.y+o2.height) or (o1.y<o2.y))
        else:
            return not(((o1.x+o1.width)<o2.x or o1.x>(o2.x+o2.width))or((o1.y+o1.height)<o2.y or o1.y > (o2.y+o2.height)))

    @classmethod
    def creaturesLearn(self, map):
        for i in map.allCreatures:
            i.brain.learn()
