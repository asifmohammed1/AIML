#Create a BankAccount class with methods for depositing money, withdrawing money, and checking the balance.
class BankAccount:
    def __init__(self, account_holder, account_number, initial_balance=0.0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive!")
            return
        self.balance += amount
        print(f"₹{amount:.2f} deposited successfully.")
        print(f"New balance: ₹{self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive!")
            return
        if amount > self.balance:
            print("Insufficient balance!")
            return
        self.balance -= amount
        print(f"₹{amount:.2f} withdrawn successfully.")
        print(f"New balance: ₹{self.balance:.2f}")
    
    def check_balance(self):
        print(f"Account Holder : {self.account_holder}")
        print(f"Account Number : {self.account_number}")
        print(f"Current Balance: ₹{self.balance:.2f}")
        print("-" * 30)
acc = BankAccount("Pravallika", "123456789012", 5000.00)
acc.check_balance()
acc.deposit(2500.50)
acc.withdraw(1800)
acc.withdraw(7000)      # should fail
acc.check_balance()


'''output:
Account Holder : Pravallika
Account Number : 123456789012
Current Balance: ₹5000.00
------------------------------
₹2500.50 deposited successfully.
New balance: ₹7500.50
₹1800.00 withdrawn successfully.
New balance: ₹5700.50
Insufficient balance!
Account Holder : Pravallika
Account Number : 123456789012
Current Balance: ₹5700.50
------------------------------'''
