from random import randint
import sys
import math
sys.path.append("Map")
from Maps.MapClass import Map

class Interactions:
    @classmethod
    def displaceScreen(Interactions,map,obstacles,creatures,displacement):
        map.x += displacement[0]
        map.y += displacement[1]
        for i in obstacles:
            i.x += displacement[0]
            i.y += displacement[1]
        for i in creatures:
            movement = Interactions.creatureMove(i,map,obstacles)
            i.x += displacement[0] + Interactions.tanh(movement[0])
            i.y += displacement[1] +Interactions.tanh(movement[1])

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
