# continues = 1
# while continues:
#     brain.calculate(initialInputs)
#     A = int(input())
#     B = int(input())
#     C = int(input())
#     brain.calculate([A,B,C])
#     contiues = input("Enter a number to continue")


#To create a nueral network you must intialize a "Brain." The 2 parameters of said brain are as goes:
# 1: a list containing the amount of nuerons you would like in each layer (including the input and output layer)
# 2: a list containing the first initial inputs you wish to be calculated

#Example:

# nueronsInEachLayer = [3,4,4,2]
# initialInputs = [.1,-2,6,.27]
# brain1 = Brain(nueronsInEachLayer, initialInputs)

#fixes to be made: activation function should not apply on the output layer but it currently does

from BrainClass import Brain

nueronsEachLayer = [2,3,2]
initialInputs = [1,1,1]

brain = Brain(nueronsEachLayer,initialInputs)

brain.getInfo()
brain.calculate(initialInputs)



