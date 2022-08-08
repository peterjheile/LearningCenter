import numpy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

# back propagation is an important word

iNodes = 2
oNodes = 2
hNodes = 3
batchSize = 1

iData = numpy.random.randn(batchSize,iNodes)
oData = numpy.random.randn(batchSize,oNodes)
print(iData)

lossArray = numpy.array([[]])
indices = numpy.array([[]])

w1 = numpy.random.randn(iNodes,hNodes)
w2 = numpy.random.randn(hNodes,oNodes)
for i in range(1000):
    hValues = iData.dot(w1)

    #rectified Linear Unit (ReLu)
    #removes all negative value and replacing them with 0

    hRelu = numpy.maximum(hValues,0)
    oDataPredicitons = hRelu.dot(w2)

    loss = numpy.square(oDataPredicitons - oData).sum()
    lossArray = numpy.append(lossArray,loss)
    indices = numpy.append(indices,i)

    #partial derivative of output predictions
    gradProd = 2 * (oDataPredicitons - oData)
    gradW2 = hRelu.T.dot(gradProd)
    gradHRelu = gradProd.dot(w2.T)
    gradHValues = gradHRelu.copy()
    gradHValues[hValues<0] = 0
    gradW1 = iData.T.dot(gradHValues)


    w1 = w1 - gradW1 * .001
    w2 = w2 - gradW2 * .001

plt.plot(indices, lossArray)
plt.legend(["Loss Over Iterations"])
plt.show()

print(oData)
print(oDataPredicitons)


# print(loss)
# # print(iData)
# # print(w1)
# # print(hRelu)
# # print(oDataPredicitons)

# x = numpy.arange(-8,8,0.1)
# y = numpy.arange(-8,8,0.1)
# x,y = numpy.meshgrid(x,y)

# z = x**2 + y **2

# #partial derivative of each x and y
# gradient = [2*x,2*y]


# axes = plt.axes(projection = "3d")
# axes.plot_surface(x,y,z)
# # derivative = 2*x
# # plt.plot(x,y,x,z)
# plt.show()
