#QUESTION06
#DESIGN CLASS
class Fruit: 
    def __init__(self, formalin=False, name=''): 
        self.__formalin = formalin 
        self.name = name
        
    def getName(self): 
        return self.name
    
    def hasFormalin(self): 
        return self.__formalin
    
class testFruit: 
    def test(self, f): 
        print('----Printing Detail----') 
        if f.hasFormalin(): 
            print('Do not eat the ',f.getName(),'.') 
            print(f)
        else: 
            print('Eat the ',f.getName(),'.') 
            print(f)

#SUBTASK
class Mango(Fruit):
    def __init__ (self, var1 = True, var2 = "Mango"):
        self._formalin = var1 
        self.name = var2
        
    def hasFormalin(self):
        if self._formalin:
            return True
        else:
            return False
        
    def __str__(self):
        if self.hasFormalin():
            return (self.name + "s are bad for you")
        else:
            return (self.name + "s are good for you")
        
class Jackfruit(Mango):
    def __init__(self, var1 = False, var2 = "Jackfruit"):
        super().__init__(var1, var2)

#MAIN CODE
m = Mango() 
j = Jackfruit() 
t1 = testFruit() 
t1.test(m) 
t1.test(j)
