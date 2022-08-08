from re import A
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

class NueralLayer:
    def __init__(self, inputs, nueronsNextLayer = 0,bias = 0):
        self.bias = bias
        self.inputs = inputs
        self.layerNuerons = [Nueron(i,nueronsNextLayer) for i in self.inputs]
        self.eachNueronValue = self.getEachNueronValue()
        self.eachNueronOutput = self.getEachNueronOutput()    
        self.nextLayerInputs = self.getNextLayerInput()
    
    #returns the input value of each nueron in the layer
    def getEachNueronValue(self):
        return [i.value for i in self.layerNuerons]
    
    #returns a list of list of the outputs of every nueron in the layer, this should be the same as the inputs of the next layer
    #each list in the list countains all of a single nueron's outputs
    def getEachNueronOutput(self):
        return [i.output for i in self.layerNuerons]

    def getNextLayerInput(self):
        input = []
        allOutputs = self.eachNueronOutput
        for i in range(len(allOutputs[0])):
            total = self.bias
            for x in range(len(allOutputs)):
                total += allOutputs[x][i] 
            input.append(self.reLU(total))
        return input

    def update(self, inputs):
        self.inputs = inputs
        for i,x in zip(self.layerNuerons,inputs):
            i.update(x)
        self.eachNueronValue = self.getEachNueronValue()
        self.eachNueronOutput = self.getEachNueronOutput()    
        self.nextLayerInputs = self.getNextLayerInput()

    def reLU(self, input):
        return max(0,input)



    def getInfo(self):
        print("Layer Inputs:",self.eachNueronValue,"\n")
        counter = 1
        for i in self.layerNuerons:
            print("Nueron", counter, "weights: ")
            print(i.weights)
            print()
            counter += 1
        print("Layer Outputs:", self.nextLayerInputs)

        
class Brain:
    def __init__(self, nueronsInEachLayer, input):
        self.nueronsInEachLayer = nueronsInEachLayer + [0]
        self.input = input
        self.allLayers = []
        self.createAllLayers(self.input)

    def createAllLayers(self, input, counter = 0):
        if counter != len(self.nueronsInEachLayer)-2:
            self.allLayers.append(NueralLayer(input,self.nueronsInEachLayer[counter+1]))
            self.createAllLayers(self.allLayers[counter].nextLayerInputs, counter+1)
        else: 
            self.allLayers.append(NueralLayer(input))

    def getInfo(self):
        counter = 1
        for i in self.allLayers:
            print("----------------------")
            print("LAYER", counter,"INFORMATION\n")
            i.getInfo()
            print("----------------------")
            counter +=1

    def calculate(self, inputs):
        print("--------------------------------------")
        print("Input: ", inputs)
        for i in self.allLayers:
            i.update(inputs)
            inputs = i.nextLayerInputs
        print("Output:",self.allLayers[len(self.allLayers)-2].nextLayerInputs)
        print("--------------------------------------")

            
nueronsEachLayer = [2,3,2]
initialInputs = [1,1,1]

brain = Brain(nueronsEachLayer,initialInputs)

continues = 1
while continues:
    brain.calculate(initialInputs)
    A = int(input())
    B = int(input())
    C = int(input())
    brain.calculate([A,B,C])
    contiues = input("Enter a number to continue")


#To create a nueral network you must intialize a "Brain." The 2 parameters of said brain are as goes:
# 1: a list containing the amount of nuerons you would like in each layer (including the input and output layer)
# 2: a list containing the first initial inputs you wish to be calculated

#Example:

# nueronsInEachLayer = [3,4,4,2]
# initialInputs = [.1,-2,6,.27]
# brain1 = Brain(nueronsInEachLayer, initialInputs)

#fixes to be made: activation function should not apply on the output layer but it currently does


        
        
    