class Interactions:
    @classmethod
    def moveScreen(Interactions, world, movement):
        world.moveAllCreatures(movement)
        world.moveAllObstacles(movement)
        

        
