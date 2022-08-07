import numpy as np

class Nueron:
    def __init__(self, value, connections = 0):
        self.value = value
        self.weights = np.random.randn(connections,)
        self.output = self.getOutputs()

    #returns a list of the output of each nueron (value * weight)
    def getOutputs(self):
        return [(i * self.value) for i in self.weights] if self.weights.any() else [self.value]

class NueralLayer:
    def __init__(self, inputs, nueronsNextLayer = 0,bias = 0):
        self.bias = bias
        self.layerNuerons = [Nueron(i,nueronsNextLayer) for i in inputs]
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
            input.append(total + self.bias)
        return input

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
        if counter != len(self.nueronsInEachLayer)-1:
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
            

nueronsEachLayer = [2,3,2]
inputs = [1,1]

brain = Brain(nueronsEachLayer,inputs)
brain.getInfo()
        
        
    