class Interactions:
    @classmethod
    def displaceScreen(Interactions,map,obstacles,displacement):
        map.x += displacement[0]
        map.y += displacement[1]

        for i in obstacles:
            i.x += displacement[0]
            i.y += displacement[1]