from NueronClass import Nueron

class NueralLayer:
    def __init__(self, inputs, nueronsNextLayer = 0, bias = 0, final = False):
        self.bias = bias
        self.inputs = inputs
        self.final = final
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

            if self.final:
                # creates variable that has not been altered by reLU to be used to calculate error
                input.append(total)
            else:
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