from multiprocessing.sharedctypes import Value
import numpy as np

class Brain:
    def __init__(self, nueronsEachLayer, brianInputs):
        self.brainInputs = brianInputs
        self.nueronsEachLayer = nueronsEachLayer + [0]
        self.allLayers = []
        self.createLayers(self.brainInputs)

    def createLayers(self, inputs, counter = 0):
        if self.nueronsEachLayer[counter+1] == 0: 
            self.allLayers.append(NueralLayer(inputs))
        else:
            layer = NueralLayer(inputs, self.nueronsEachLayer[counter], self.nueronsEachLayer[counter+1])
            self.allLayers.append(layer)
            self.createLayers(layer.layerOutputs,counter+1)

    def getInfo(self):
        counter = 0
        for i in self.allLayers:
            print("--------------------------")
            print("LAYER ",counter , "\n")
            print("Layer Values: ", i.layerOutputs)
            print("Nueron Outputs: ", i.allNueronOutputs)
            for x in i:
                print(Nueron)
            print("--------------------------")
            counter+=1
        

class NueralLayer:
    def __init__(self,inputs, nueronsNextLayer = 0,bias = 0):
        self.bias = bias
        self.layerNuerons = [Nueron(i,nueronsNextLayer) for i in inputs]
        self.allNueronOutputs = self.getAllNueronOutputs()
        self.layerOutputs = self.getLayerOutputs()

    def getAllNueronOutputs(self):
        return [i.getOutputs() for i in self.layerNuerons]

    def getLayerOutputs(self):
        layerOutputs = []
        for i in range(len(self.allNueronOutputs[0])):
            output = 0
            for x in range(len(self.allNueronOutputs)):
                output += self.allNueronOutputs[x][i]
            layerOutputs.append(output + self.bias)
        return layerOutputs

class Nueron:

    def __init__(self, value, connections = 0):
        self.value = value
        self.weights = np.random.randn(connections,)

    def getOutputs(self):
        return [(i * self.value) for i in self.weights] if self.weights.any() else [self.value]

X = [1,.5]

brain = Brain([2,4,2],X)
brain.getInfo()



