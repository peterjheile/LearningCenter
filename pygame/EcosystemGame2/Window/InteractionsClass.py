from random import randint
import sys
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
            i.x += displacement[0] + Interactions.creatureMove()
            i.y += displacement[1] + Interactions.creatureMove()

    @classmethod
    def creatureMove(Interactions):
        return randint(-1,1)

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
