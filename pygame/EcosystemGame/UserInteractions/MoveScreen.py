class Interactions:
    @classmethod
    #moves everything on screen and updates their coordinates to appear to be moving the screen
    def moveScreen(Interactions, world, movement):
        #moves all creatures
        for i in world.allCreatures:
            i.setX(i.getX() + movement[0])
            i.setY(i.getY() + movement[1])
        #move all creatures
        for i in world.allObstacles:
            i.setX(i.getX() + movement[0])
            i.setY(i.getY() + movement[1])

        #moves backgroun map
        world.map.setX(world.map.getX() + movement[0])
        world.map.setY(world.map.getY() + movement[1])



        
