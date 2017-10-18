
class BankAccount:

    def __init__(self,name, password):
        self.balance = 0
        self.name = name
        self.__password = password

    def __str__(self):
        return [self.password,self.balance]

    def showBalance(self):
        return self.balance

    def withdraw(self, amount):
        if 0 <= amount <= self.balance:
            self.balance -= amount
            return True
        else:
            print "You're current balance is %s you dont have enough funds" % self.balance
            return False

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            return True
        else:
            print "Please enter a positive value!"
            return False

# a = BankAccount("1111")
# print(a.deposit(200))
# print(a.showBalance())
# print(a.withdraw(10))
# print(a.showBalance())