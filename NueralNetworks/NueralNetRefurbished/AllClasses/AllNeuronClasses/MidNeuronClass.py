from AllNeuronClasses.NeuronClass import Neuron
import numpy as np

class MidNeuron(Neuron):
    def __init__(self, input, connections):
        super().__init__(input)
        self.weights = np.random.randn(connections,)
        # print("MidNueron Created")
        # print(self.weights)
        self.output = self.calculateOutput()

    def calculateOutput(self):
        return [(self.value*i) for i in self.weights]