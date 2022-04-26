#This code converts a number of any base into decimal base 10

def convertToDecimal():
    numberToConvert = str(input("Enter a number to input: "))
    currentBase = int(input("Enter the current base (you must be using the hexidecimal symbols and only works to base 16): "))

    dictSymbols = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,"A":10,"B":11,'C':12,"D":13,"E":14,"F":15}
    return sum([dictSymbols[z]*(currentBase**i) for i,z in zip(range(len(numberToConvert)),numberToConvert[::-1])])

print(convertToDecimal())
