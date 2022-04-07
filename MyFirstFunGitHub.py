#This code converts a number of any base into decimal base 10

from unicodedata import numeric
def convertToDecimal():
    numberToConvert = input("Enter a number to input")
    currentBase = input("Enter the current base")
    dictSymbols = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,"A":10,"B":11,'C':12,"D":13,"E":14,"F":15}
    return sum([dict[z]*(currentBase**i) for i,z in zip(range(len(numberToConvert)),numberToConvert[::-1])])

    # print(dictSymbols)

    # return sum([dict[z]*(currentBase**i) for i,z in zip(range(len(numberToConvert)),numberToConvert[::-1])])
