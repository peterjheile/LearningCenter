import numpy as np

class Nueron:
    def __init__(self, value, connections = 0):
        self.value = value
        self.weights = np.random.randn(connections,)
        self.output = self.getOutputs()

    #returns a list of the output of each nueron (value * weight)
    def getOutputs(self):
        return [(i * self.value) for i in self.weights] if self.weights.any() else [self.value]

    def update(self, value):
        self.value = value
        self.output = self.getOutputs()