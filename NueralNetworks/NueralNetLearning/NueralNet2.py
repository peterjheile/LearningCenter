#Input Data denoted by X
#Data should be scaled to between (-1,1) because it scales exponentially in NN
#This prevents outrageously large numbers

#the same thing goes for weights, they need to be small
#biases are usually initialized as 0, although sometimes it shouldnt be
#because it can kill the network

#activation functions define the output of a nueron, if it is negative
#the nueron does not fire meaning it is generalized to 0
#examples are the sigmoid function, step function, and ReLU (the most common)

#optomizers is an algorithm/function the changes the weights and biases 
#to minimize the loss

#Normalization converts a number to a number between (0,1)

#Categorial cross-entropy -Log(yi,k)   (aka negative log) to calculate loss

#One-hot encoding     A vector with a single 1 and the rest 0s

import numpy as np
import nnfs
from nnfs.datasets import spiral_data
import math

nnfs.init()
np.random.seed(0)

#Creates data 
# X, y = spiral_data(100, 3)   

#exmponential function gets rid of negative numbers without losing
#the meaning of a negatie vvalue
# E = math.e

# X = [[1,2,3,2.5],
#      [2.0,5.0,-1.0,2.0],
#      [-1.5,2.7,3.3,-0.8]]

# print(X)


class LayerDense:
    def __init__(self, n_inputs, n_nuerons):
        self.weights = 0.1 * np.random.randn(n_inputs,n_nuerons)
        self.biases = np.zeros((1, n_nuerons))

    def forward(self, inputs):
        self.output = np.dot(inputs,self.weights) + self.biases


class AcitvationReLU:
    def forward(self, inputs):
        self.output = np.maximum(0,inputs)


class ActivationSoftMax:
    def forward(self, inputs):
        expValues = np.exp(inputs - np.max(inputs, axis = 1, keepdims = True))
        probabilities = expValues/np.sum(expValues , axis = 1, keepdims = True)
        self.output = probabilities
 
class Loss:
    def calculate(self, output, y):
        sampleLosses = self.forward(output,y)
        dataLoss = np.mean(sampleLosses)
        return dataLoss

class LossCategoricalCorssEntorpy(Loss):
    def forward(self,yPred,yTrue):
        samples = len(yPred)
        yPredClipped = np.clip(yPred, math.e**-7, 1- math.e**-7)

        if len(yTrue.shape) == 1:
            correctConfidences = yPredClipped[range(samples), yTrue]
        else:
            correctConfidences = np.sum(yPredClipped*yTrue, axis = 1)

        negativeLogLiklihood = -np.log(correctConfidences)
        print(negativeLogLiklihood)
        return negativeLogLiklihood



X,y = spiral_data(samples = 100, classes = 3)

dense1 = LayerDense(2,3)
activation1 = AcitvationReLU()
dense2 = LayerDense(3,3)
activation2 = ActivationSoftMax()

dense1.forward(X)
activation1.forward(dense1.output)

dense2.forward(activation1.output)
activation2.forward(dense2.output)

# print(activation2.output[:5])

lossFunction = LossCategoricalCorssEntorpy()
loss = lossFunction.calculate(activation2.output,y)

# print("Loss: ",loss)












