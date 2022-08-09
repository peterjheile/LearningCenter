from Things.NueralNetCreator.LayerClass import NueralLayer

class Brain:
    def __init__(self, nueronsInEachLayer, input):
        self.nueronsInEachLayer = nueronsInEachLayer + [0]
        self.input = input
        self.allLayers = []
        self.createAllLayers(self.input)

    def createAllLayers(self, input, counter = 0):
        if counter != len(self.nueronsInEachLayer)-2:
            if counter == len(self.nueronsInEachLayer)-3:
                self.allLayers.append(NueralLayer(input,self.nueronsInEachLayer[counter+1],final = True))
                self.createAllLayers(self.allLayers[counter].nextLayerInputs, counter+1)
            else:
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

    # def calculate(self, inputs):
    #     print("--------------------------------------")
    #     print("Input: ", inputs)
        # for i in self.allLayers:
        #     i.update(inputs)
        #     inputs = i.nextLayerInputs
    #     print("Output:",self.allLayers[len(self.allLayers)-2].nextLayerInputs)
    #     print("--------------------------------------")

    def calculate(self,inputs):
        for i in self.allLayers:
            i.update(inputs)
            inputs = i.nextLayerInputs
        return self.allLayers[len(self.allLayers)-2].nextLayerInputs
