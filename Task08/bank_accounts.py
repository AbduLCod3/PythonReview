class BalanceException(Exception):
    ...




class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName

        print(f"\nAccount '{self.name}' created. \nBalance = ${self.balance:.2f}")
    
    def getBalance(self):
        print(f"\nAccount '{self.name}' Balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit Complete.")
        self.getBalance()
        print("\n")

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}")
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance -  amount
            print('Withdrawal Completed.\n')

        except BalanceException as error:
            print(f'\nWithdrawal interrupted: {error}\n')

    
    def transfer(self, amount, account):
        try:
            print('\n**********\n\nBegining Transfer... 🚀')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer Completed!\n\n**********\n')
        except BalanceException as error:
            print(f'\nTransfer interrupted: {error}. ❌\n')

class interestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print(f'\nDeposit Completed.')
        self.getBalance()


class SavingsAccount(interestRewardsAcct):
    def __init(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print('\nWithdrawal Completed.')
            self.getBalance()

        except BalanceException as error:
            print(f'\nWithdrawal interrupted: {error}. ❌\n')