from Bank import Bank
from BankAccount import BankAccount


class ATM(Bank,BankAccount):
    def __init__(self, bank):
        self.account = None
        self.bank = bank
        self.methods = {}
        self.methods["1"] = self._showBalance
        self.methods["2"] = self._deposit
        self.methods["3"] = self._withdraw

    def startMenu(self):
        while True:
            print("""
                1. Login
                2. Quit
                """)
            choice = checkForInt("Please enter your choice")
            if choice=="1":
                self.passwordCheck()
            elif choice == "2":
                quit()
            else:
                print "You must select 1 or 2"

    def passwordCheck(self):
        while True:
            password = checkForInt("Please enter your pin code")
            if len(password) != 4:
                print "pin code must contain 4 digits"
            elif password in self.bank.accounts:
                self.account = self.bank.accounts[password]
                break
            else:
                print "Wrong pin code! please try again"

        self.mainMenu()

    def mainMenu(self):
        while True:
            self.printMainMenu()
            choice = int(checkForInt("Please choose what action you would like to perform"))
            if choice>0 and choice<4:
                self.methods[str(choice)]()
            elif choice==4:
                print "Have a great day %s" % self.account.name
                self.account = None
                break
            else:
                print "please choose a number between 1-4"

    def printMainMenu(self):
        print ("""
            Hello %s

            1. Check Balance
            2. Deposit
            3. Withdrawl
            4. LogOff

            You can type "0" in any screen to return to main menu

            """ % self.account.name)

    def _showBalance(self):
        print "Your current balance is %s" % self.account.showBalance()

    def _deposit(self):
        while True:
            amount = int(checkForInt("Please enter the amount you want to deposit"))
            if amount is 0:
                break
            if self.account.deposit(amount):
                print "Success"
                break
            else:
                pass

    def _withdraw(self):
        while True:
            amount = int(checkForInt("Please enter the amount you want to withdraw"))
            if amount is 0:
                break
            if self.account.withdraw(amount):
                print "Success"
                break
            else:
                pass


def checkForInt(message):
    while True:
        choice = raw_input(message)
        if choice.isdigit():
            break
        else:
            print "The input you entered is not valid, Numbers only please!"

    return choice

if __name__ == "__main__":
    a = Bank()
    b = BankAccount("Ido","1111")
    c = BankAccount("Arbel","2222")

    a.addAccount(b)
    a.addAccount(c)

    d = ATM(a)
    d.startMenu()



