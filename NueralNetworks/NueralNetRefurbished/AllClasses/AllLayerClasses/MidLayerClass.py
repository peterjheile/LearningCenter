from sys import getallocatedblocks
import sys 
sys.path.append("C:\\Users\\peter\\OneDrive\\Documents\\Peter Heile GitHub\\LearningCenter")
from NueralNetworks.NueralNetRefurbished.AllClasses.AllLayerClasses.LayerClass import Layer
from NueralNetworks.NueralNetRefurbished.AllClasses.AllNeuronClasses.MidNeuronClass import MidNeuron
import random

class MidLayer(Layer):
    def __init__(self, inputs, connections):
        super().__init__(inputs)
        self.connections = connections
        self.layerBias = .01
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
            summedOutputs.append(x.activationFunction(sum(outputs)+self.layerBias))
            outputs = []
        return summedOutputs

#updates the input values of each neuron and gets a list of the new outputs based on those values
    def calculate(self, inputs):
        for i in range(len(self.allNeurons)):
            self.allNeurons[i].value = inputs[i]
            self.allNeurons[i].output = self.allNeurons[i].calculateOutput()
        self.layerOutputs = self.getAllOutputs()

#adjusts the weights of each neuron by a tiny amount (randomly)
    def learn(self):
        self.layerBias += random.uniform(-.1,.1)
        for i in self.allNeurons:
            i.learn()



