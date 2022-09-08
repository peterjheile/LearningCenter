from random import randint
import sys
import math
import pygame
sys.path.append("Map")
sys.path.append("AllObstacles")
sys.path.append("AllCreatures")
sys.path.append("Generators")
from AllObstacles.FoodClass import Food
from AllCreatures.CreatureClass import Creature
from Generators.GeneratorClass import Generator

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
                    i.x += displacement[0] + Interactions.adjustMovements(zoom,map,movement[0])*5
                    i.y += displacement[1] + Interactions.adjustMovements(zoom,map,movement[1])*5
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
    def creatureMove(Interactions,i,map,obstacles):
        movement = Interactions.getMoveFactors(i,map)
        return i.brain.calculateOutput(movement)


    # @classmethod
    # def convertToAngle(self,angle,cre,other):



#maybe instead of angle do the x and y coords
    # @classmethod
    # def getAngleAndDist(self,cre,other):
    #     xDist = (cre.x-other.x) if (cre.x-other.x) != 0 else 1
    #     yDist = cre.y - other.y
    #     distance = math.dist((cre.x,cre.y),(other.x,other.y))
    #     return (distance,Interactions(math.atan((yDist/xDist))))

    @classmethod
    def getMoveFactors(Interactions,cre,map):
        #distance to each side of the map
        centerX,centerY = map.x+(map.width/2),map.y+(map.height/2)
        midDistX = cre.x - centerX
        midDistY = cre.y - centerY
        centerDist = math.dist((cre.x,cre.y),(midDistX,midDistY))
        # centerAngle = math.degrees(math.atan((yDist/xDist)))

        #distance and angle of the closest obstacle
        obsDistX,obsDistY,obsDist = 100000,100000,100000
        for obs in map.allObstacles:
            tempDist = math.dist((cre.x,cre.y),(obs.x,obs.y))
            if tempDist < obsDist:
                obsDistX,obsDistY,obsDist = cre.x - obs.x, cre.y - obs.y, tempDist

        #distance and angle of the closest food
        foodDistX,foodDistY,foodDist = 100000,100000,100000
        for food in map.allFood:
            tempDist = math.dist((cre.x,cre.y),(food.x,food.y))
            if tempDist < foodDist:
                foodDistX,foodDistY,foodDist = cre.x - food.x, cre.y - food.y, tempDist

        #gets the creature's energy
        energy = cre.energy

        factors = [midDistX,midDistY, centerDist,obsDistX,obsDistY,obsDist,foodDistX,foodDistY,foodDist]
        updatedFactors = [(i*map.zoom)/(1000*map.zoom) for i in factors]
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
            if ((o1.x+o1.width>o2.x+o2.width) or (o1.x<o2.x) or (o1.y+o1.height>o2.y+o2.height) or (o1.y<o2.y)):
                # if o1.x<o2.x+1:
                #     o1.x = o2.x+2
                # elif o1.y<o2.y+1:
                #     o1.y = o2.y+2
                # elif o1.x>o2.x+o2.width-1:
                #     o1.x = o2.x+o2.width-2
                # elif o1.y>o2.y+o2.height-1:
                #     o1.y = o2.y+o2.height-2
                o2.allCreatures.remove(o1)
        else:
            return not(((o1.x+o1.width)<o2.x or o1.x>(o2.x+o2.width))or((o1.y+o1.height)<o2.y or o1.y > (o2.y+o2.height)))

    @classmethod
    def creaturesLearn(self, map,toLearn):
        for i in map.allCreatures[toLearn:]:
            i.brain.learn()

    @classmethod
    def reproduce(self,map):
        pass
        # numCreatures = len(map.allCreatures)
        # for i in range(numCreatures):
        #     other = copy.deepcopy(map.allCreatures[i])
        #     other.x += randint(-50,50)
        #     other.y += randint(-50,50)
        #     map.allCreatures.append(other)

    @classmethod
    def checkFoodCollision(self,map, allFood, cre):
        for i in allFood:
            if Interactions.checkCollision(cre,i):
                allFood.remove(i)
                allFood.append(Food(map.width,map.height,map.x,map.y,map.zoom))
                cre.energy += 1000
                cre.foodEaten += 1
                # for _ in range(0,4):
                #     cre = copy.deepcopy(cre)
                #     cre.x += randint(-300,300)
                #     cre.y += randint(-300,300)
                #     cre.brain.learn()
                #     map.allCreatures.append(cre)
    @classmethod
    def newGenBest(self,window,allCreatures,bestCreature):
        bestCreature = bestCreature
        totalFoodEaten = 0
        averageFoodEaten = 0
        for i in window.map.allCreatures:
            totalFoodEaten+=i.foodEaten
            if bestCreature.foodEaten<=i.foodEaten:
                bestCreature = i
        averageFoodEaten = totalFoodEaten/len(window.map.allCreatures) if len(window.map.allCreatures) >0 else 0
        survivors = len(window.map.allCreatures)

        window.map.allCreatures = []
        temp = copy.deepcopy(bestCreature)
        temp.x = randint(int(window.map.x),int(window.map.x+window.map.width))
        temp.y = randint(int(window.map.y),int(window.map.y+window.map.height))
        temp.width = 10*window.map.zoom
        temp.height = temp.width
        temp.energy = 500
        temp.foodEaten = 0
        window.map.allCreatures.append(temp)
        for i in range(10):
            cre = copy.deepcopy(bestCreature)
            cre.x = randint(int(window.map.x),int(window.map.x+window.map.width))
            cre.y = randint(int(window.map.y),int(window.map.y+window.map.height))
            cre.brain.learn()
            cre.width = 10*window.map.zoom
            cre.height = cre.width
            cre.energy = 500
            cre.foodEaten = 0
            window.map.allCreatures.append(cre)
            
        return bestCreature,survivors,totalFoodEaten,averageFoodEaten

    @classmethod
    def getAllCreatures(self,window):
        lst = []
        for i in window.map.allCreatures:
            lst.append(i)
        return lst

        


                
            


