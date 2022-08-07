import numpy as np

class NueralNetwork():

    def __init__(self):
        np.random.seed(1)

        self.synaptic_weights = 2 * np.random.random((3,1)) - 1

    def sigmoid(self,x):
        return 1/(1+np.exp(-x))

    def sigmoid_derivative(self,x):
        return x * (1-x)

    def train(self,training_inputs,training_outputs,training_iterations):

        for iteration in range(training_iterations):

            output = self.think(training_inputs)
            error = training_outputs - output

            adjustments = np.dot(training_inputs.T,error*self.sigmoid(output))
            self.synaptic_weights += adjustments

    def think(self, inputs):

        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs,self.synaptic_weights))

        return output
# from nueralNet import NueralNetwork
if __name__ == "__main__":
    nueral_network = NueralNetwork()

    print("Random synaptic weights")
    print(nueral_network.synaptic_weights)

    training_inputs = np.array([[0,0,1],
                            [1,1,1],
                            [1,0,1],
                            [0,1,1]])

    training_outputs = np.array([[0,1,1,0]]).T

    nueral_network.train(training_inputs,training_outputs, 10000)

    print("Synaptic weights after training: ")
    print(nueral_network.synaptic_weights)

    A = str(input("input 1: "))
    B = str(input("input 2: "))
    C = str(input("input 3: "))

    print("New Situation: input data = ",A, B, C)
    print("Output Data: ")
    print(nueral_network.think(np.array([A,B,C])))
