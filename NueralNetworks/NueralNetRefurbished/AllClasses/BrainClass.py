import sys

sys.path.append("AllLayerClasses")
sys.path.append("AllNeuronClasses")

from AllLayerClasses.MidLayerClass import MidLayer
from AllLayerClasses.FinalLayerClass import FinalLayer
from AllNeuronClasses.FinalNeuronClass import FinalNeuron

class Brain:
    def __init__(self, neuronsEachLayer, initialInputs):
        self.initialInputs = initialInputs
        self.neuronsEachLayer = neuronsEachLayer
        self.Layers = []
        self.createLayers(self.initialInputs,self.neuronsEachLayer)

    def createLayers(self, inputs, neuronsEachLayer):
        if (len(neuronsEachLayer) == 1):
            self.finalLayer = FinalLayer(inputs)
            self.Layers.append(self.finalLayer)
        else:
            layer = MidLayer(inputs,neuronsEachLayer[1])
            self.Layers.append(layer)
            self.createLayers(layer.layerOutputs, neuronsEachLayer[1:])

    def calculate(self, inputs):
        self.initialInputs = inputs
        for i in self.Layers:
            i.calculate(inputs)
            inputs = i.layerOutputs
        return self.Layers[len(self.Layers)-1].layerOutputs

    def learn(self):
        for i in range(len(self.Layers)-1):
            self.Layers[i].learn()
        self.calculate(self.initialInputs)


    def getInfo(self):
        for i in range(len(self.Layers)):
            print("------------------------")
            print("Layer", i)
            for x in range(len(self.Layers[i].allNeurons)):
                print("Nueron", x)
                print("Nueron Value:",self.Layers[i].allNeurons[x].value)
                if not(isinstance(self.Layers[i].allNeurons[x],FinalNeuron)):
                    print("Nueron Weights:",self.Layers[i].allNeurons[x].weights)
                print("Neuron Output:", self.Layers[i].allNeurons[x].output)
    


            
brain = Brain([5,8,8,3], [1,2,3,4,5])
print(brain.calculate([1,2,3,4,5]))
print(brain.calculate([-1,3,1,.02,-.99]))












