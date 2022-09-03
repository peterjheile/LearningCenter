from random import randint
import sys
import math
import pygame
sys.path.append("Map")
sys.path.append("AllObstacles")
sys.path.append("AllCreatures")
from AllObstacles.FoodClass import Food
from AllCreatures.CreatureClass import Creature

from Maps.MapClass import Map
import copy


class Interactions:
    @classmethod
    def displaceScreen(Interactions,map,obstacles,creatures,displacement, all,zoom = 0):
        Interactions.zoom(map,zoom)
        map.x += displacement[0]
        map.y += displacement[1]
        for i in obstacles:
            i.x += displacement[0]
            i.y += displacement[1]
        for i in map.allFood:
            i.x += displacement[0]
            i.y += displacement[1]
        for i in creatures:
            movement = Interactions.creatureMove(i,map,obstacles)
            if all:
                if i.energy >0:
                    i.x += displacement[0] + Interactions.adjustMovements(zoom,map,Interactions.tanh(movement[0]))
                    i.y += displacement[1] + Interactions.adjustMovements(zoom,map,Interactions.tanh(movement[1]))
                    i.energy -= (1*map.zoom)
                    Interactions.checkFoodCollision(map,map.allFood,i)
                else:
                    map.allCreatures.remove(i)
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
            for i in map.allFood:
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
            for i in map.allFood:
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

        #gets the closest Food and passes it as a move factor
        closestFood, obsFood,distance = 100000,map.allFood[0],100000
        for food in map.allFood:
            distance = math.dist((cre.x,cre.y),(food.x,food.y))
            if distance < closestFood:
                closestFood, obsFood = distance,food
            closestFood = closestFood

        #gets the angle of the closest food
        xDist = (obsFood.x - cre.x) if (obsFood.x - cre.x != 0) else 1
        yDist = (obsFood.y - cre.y)
        angleFood = math.degrees((math.atan(abs(yDist)/abs(xDist))))
        if (xDist < 0 and yDist > 0):
            angleFood = angleFood+90
        elif (xDist < 0 and yDist < 0):
            angleFood = angleFood + 180
        elif (xDist > 0 and yDist < 0):
            angleFood = angleFood + 270


        #distance to each side of the map
        lBord = (cre.x - map.x)
        rBord = (map.x+map.width) - cre.x
        tBord = (cre.y - map.y)
        bBord = (map.y+map.height) - cre.y

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

        factors = [angle, closest, lBord, rBord, tBord, bBord, angleFood, closestFood,cre.energy]
        updatedFactors = [i*map.zoom for i in factors]
        
        return updatedFactors
        

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

    @classmethod
    def reproduce(self,map):
        numCreatures = len(map.allCreatures)
        for i in range(numCreatures):
            other = copy.deepcopy(map.allCreatures[i])
            other.x += 20
            map.allCreatures.append(other)

    @classmethod
    def checkFoodCollision(self,map, allFood, cre):
        for i in allFood:
            if Interactions.checkCollision(cre,i):
                cre.energy += 1000
                allFood.remove(i)
                allFood.append(Food(map.width,map.height,map.x,map.y,map.zoom))
                cre = copy.deepcopy(cre)
                cre.x += 30
                map.allCreatures.append(cre)

                
            


