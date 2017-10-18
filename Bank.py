

class Bank:

    def __init__(self):
        self.accounts = {}

    def addAccount(self,account):
        self.accounts[account.__password] = account

    def showAccounts(self):
        for account in self.accounts:
            print account.__str__()
# a = Bank()
# b = BankAccount("ido","1111")
# c = BankAccount("arbel","2222")
#
# a.addAccount(b)
# a.addAccount(c)
# print(a.accounts["1111"])
# a.showAccount()