import sys
sys.path.append("C:\\Users\\peter\\OneDrive\\Documents\\Peter Heile GitHub\\LearningCenter")
from NueralNetworks.NueralNetRefurbished.AllClasses.AllNeuronClasses.NeuronClass import Neuron
import math

class FinalNeuron(Neuron):
    def __init__(self, input):
        super().__init__(input)
        self.output = self.calculateOutput()

    def calculateOutput(self):
        return self.value

#uses the sigmoid acitvation function for the final layer
    def activationFunction(self, value):
        return value







        