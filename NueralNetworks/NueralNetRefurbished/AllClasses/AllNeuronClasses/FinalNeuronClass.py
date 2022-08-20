from AllNeuronClasses.NeuronClass import Neuron

class FinalNeuron(Neuron):
    def __init__(self, input):
        super().__init__(input)
        self.output = self.calculateOutput()

    def calculateOutput(self):
        return self.value



        