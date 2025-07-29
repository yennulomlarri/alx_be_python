# bank_account.py

class BankAccount:
    """A class to represent a simple bank account."""

    def __init__(self, initial_balance=0):
        """Initializes the bank account with an optional initial balance."""
        self.account_balance = float(initial_balance)

    def deposit(self, amount):
        """Adds the specified amount to the account balance."""
        if amount > 0:
            self.account_balance += amount
        else:
            # This part is for robust handling, not strictly required by prompt
            # but good practice.
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Deducts the amount from the balance if funds are sufficient.
        Returns True for a successful withdrawal, False otherwise.
        """
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Prints the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance:.2f}")