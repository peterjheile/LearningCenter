from random import randint

import random

class Background:
    def __init__(self):
        self.background_color = (0,200,50)
        #goes in order of left border, right border, top border, bottom border
        self.borderLocations = [randint(-1000,-500),randint(500,1000),randint(-1000,-500),randint(500,1000)]

    def get_background_color(self):
        return self.background_color

    def get_border_locations(self):
        return self.borderLocations

    def create_Borders(self):
        pass
