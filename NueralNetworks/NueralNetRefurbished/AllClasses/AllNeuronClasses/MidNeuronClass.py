from AllNeuronClasses.NeuronClass import Neuron
import numpy as np
import random
import math

class MidNeuron(Neuron):
    def __init__(self, input, connections):
        super().__init__(input)
        self.weights = np.random.randn(connections,)
        # print("MidNueron Created")
        # print(self.weights)
        self.output = self.calculateOutput()

    def calculateOutput(self):
        return [(self.value*i) for i in self.weights]

    def learn(self):
        for i in range(len(self.weights)):
            self.weights[i] = self.weights[i] + random.uniform(-.01,.01)

#uses the reLU activation function for mid layer nuerons
    def activationFunction(self, value):
        return ((math.e**value - math.e**-value)/(math.e**value + math.e**-value))