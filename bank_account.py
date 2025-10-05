# bank_account.py

class BankAccount:
    """A class that represents a simple bank account."""

    def __init__(self, initial_balance=0):
        """Initialize the account with an initial balance (default is zero)."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit a specified amount into the account."""
        if amount > 0:
            self.account_balance += amount
        else:
            print("❌ The amount must be positive!")

    def withdraw(self, amount):
        """Withdraw a specified amount if sufficient funds are available."""
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Display the current account balance."""
        print(f"💰 Current Balance: ${self.account_balance}")
