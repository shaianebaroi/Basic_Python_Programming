#QUESTION04
#DESIGN CLASS

class Account:
    def __init__(self,balance):
        self._balance = balance
    def getBalance(self):
        return self._balance

#SUBTASK
class CheckingAccount (Account):
    numberOfAccount = str(0)
    
    def __init__(self, balance = 0.00):
        self._balance = float(balance)
        CheckingAccount.numberOfAccount = int (CheckingAccount.numberOfAccount)       
        CheckingAccount.numberOfAccount += 1
        CheckingAccount.numberOfAccount = str (CheckingAccount.numberOfAccount)
        
    def __str__(self):
        return ("Account Balance: " + str(self.getBalance()))

#MAIN CODE
print('Number of Checking Accounts: '+CheckingAccount.numberOfAccount)
print(CheckingAccount())
print(CheckingAccount(100.00))
print(CheckingAccount(200.00))
print('Number of Checking Accounts: '+CheckingAccount.numberOfAccount)
