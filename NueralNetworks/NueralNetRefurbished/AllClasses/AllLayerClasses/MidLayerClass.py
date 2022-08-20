from sys import getallocatedblocks
import sys 
sys.path.append("AllNeuronClasses")
from AllLayerClasses.LayerClass import Layer
from AllNeuronClasses.MidNeuronClass import MidNeuron

class MidLayer(Layer):
    def __init__(self, inputs, connections):
        super().__init__(inputs)
        self.connections = connections
        self.allNeurons = self.createLayer()
        self.layerOutputs = self.getAllOutputs()

    def createLayer(self):
        return [MidNeuron(self.inputs[i], self.connections) for i in range(self.numNeurons)]

#gets a list of the outputs of each neuron added together
#this is the next layer inputs
    def getAllOutputs(self):
        outputs = []
        summedOutputs = []
        for i in range(self.connections):
            for x in self.allNeurons:
                outputs.append((x.value * x.weights[i]))
            summedOutputs.append(sum(outputs))
            outputs = []
        return summedOutputs

#updates the input values of each neuron and gets a list of the new outputs based on those values
    def calculate(self, inputs):
        for i in range(len(self.allNeurons)):
            self.allNeurons[i].value = inputs[i]
            self.allNeurons[i].output = self.allNeurons[i].calculateOutput()
        self.layerOutputs = self.getAllOutputs()

