from random import randint
import random
import numpy as np
import copy
import math

class Brain:
    def __init__(self,layersAndSizes):
        self.layersAndSizes = layersAndSizes
        self.createNuerons()
        self.createWeights()
        self.createBiases()

    def createNuerons(self):
        self.allLayers = []
        for i in self.layersAndSizes:
            self.allLayers += [[randint(-5,5) for _ in range(i)]]

    def createWeights(self):
        self.allWeights = []
        for i in range(len(self.layersAndSizes)-1):
            self.allWeights += [[[randint(-1,1) for _ in range(self.layersAndSizes[i+1])] for _ in range(self.layersAndSizes[i])]]

    def createBiases(self):
        self.allBiases = []
        for _ in range(len(self.layersAndSizes)-1):
            self.allBiases += [.1]

    def calculateOutput(self,input):
        self.allLayers[0] = input
        for a in range(1,len(self.allLayers)):
            newLayer = []
            for b in range(len(self.allLayers[a])):
                total = self.allBiases[a-1]
                for c in range(len(self.allLayers[a-1])):
                    num1 = self.allLayers[a-1][c]
                    num2 = self.allWeights[a-1][c][b]
                    total += num1*num2
                newLayer.append(self.tanh(total))
            self.allLayers[a] = copy.deepcopy(newLayer)  
        return self.allLayers[len(self.allLayers)-1]

    def tanh(self,x):
        return (math.e**x-math.e**-x)/(math.e**x+math.e**-x)

#edits every weight and bias by a small random amount
    def learn(self):
        for a in range(0,len(self.allWeights)):
            for b in range(0,len(self.allWeights[a])):
                for c in range(0,len(self.allWeights[a][b])):
                    self.allWeights[a][b][c] += random.uniform(-1,1)
        for a in range(0,len(self.allBiases)):
            self.allBiases[a] += random.uniform(-.1,.1)

#edits a random weight and random bias by a small random amount
    # def learn(self):
    #     n1 = randint(1,len(self.allWeights)-1)
    #     n2 = randint(1,len(self.allWeights[n1])-1)
    #     n3 = randint(1,len(self.allWeights[n1][n2])-1)
    #     m = randint(1,len(self.allBiases)-1)
    #     self.allWeights[n1][n2][n3] += random.uniform(-1,1)
    #     self.allBiases[m] += random.uniform(-.1,.1)

    def print(self):
        print("Layers")
        print(self.allLayers)
        print("weights")
        print(self.allWeights)
        print("Biases")
        print(self.allBiases)
        


