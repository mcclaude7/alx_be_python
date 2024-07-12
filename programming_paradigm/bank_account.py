class BankAccount:
    def __init__(self, initial_balance = 0):
        self.account_balance = initial_balance
    def deposit(self, amount):
        if amount > 0:
            account_balance = account_balance + amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit must be positive.")


    def withdraw(self,amount):
        if amount > 0:
            if self.account_balance >= amount:
               self.account_balance -= amount
               print(f"Withdraw: {amount}")
               return True
            else:
                print("Insufficient funds")
                return False
            
    def display_balance(self):
        print(f"current balance: {self.account_balance}")
