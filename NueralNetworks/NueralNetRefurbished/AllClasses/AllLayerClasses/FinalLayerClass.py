import sys

sys.path.append("AllNeuronClasses")

from AllLayerClasses.LayerClass import Layer
from AllNeuronClasses.FinalNeuronClass import FinalNeuron

class FinalLayer(Layer):
    def __init__(self, inputs):
        super().__init__(inputs)
        self.allNeurons = self.createLayer()
        self.layerBias = 1
        self.layerOutputs = self.getAllOutputs()


    def createLayer(self):
        return [FinalNeuron(self.inputs[i]) for i in range(self.numNeurons)]

    def getAllOutputs(self):
        return [i.activationFunction(i.value + self.layerBias) for i in self.allNeurons]

#updates the input values of each neuron and gets a list of the new outputs based on those values
    def calculate(self, inputs):
        for i in range(len(self.allNeurons)):
            self.allNeurons[i].value = inputs[i]
            self.allNeurons[i].output = self.allNeurons[i].calculateOutput()
        self.layerOutputs = self.getAllOutputs()

