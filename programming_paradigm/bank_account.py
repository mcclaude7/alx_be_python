class BankAccount:
    def __init__(self, initial_balance = 0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount > 0:
            if self.account_balance >= amount:
                self.account_balance -= amount
                print(f"Withdrawal: {amount}")
                return True
            else:
                return False
        
        else:
            print("withdrawal amount must be positive")
            return False
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")


            
