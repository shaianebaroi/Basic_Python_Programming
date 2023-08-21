#QUESTION03
#DESIGN CLASS
class RealNumber:
    def __init__(self, r=0):
        self.__realValue = r
    def getRealValue(self):
        return self.__realValue
    def setRealValue(self, r):
        self.__realValue = r
    def ping(self):
        print('I am in RealNumber class')
    def __str__(self):
        return 'RealPart: '+str(self.getRealValue())

#SUBTASK
class ComplexNumber (RealNumber):
    def __init__(self, var1 = 1, var2 = 1):
        self.setRealValue(var1)
        self.setImaginaryValue(var2)
        
    def getImaginaryValue(self):
        return self.__iValue
    
    def setImaginaryValue(self, var3):
        self.__iValue = var3
        
    def ping(self):
        print("I am in RealNumber class")
        
    def __str__(self):
        return ("RealPart: " + str(float(self.getRealValue()))) + '\nImaginaryPart: ' + str(float(self.getImaginaryValue()))

cn1 = ComplexNumber()
print(cn1)
print('---------')

cn2 = ComplexNumber(5,7)
print(cn2)
print('---------')