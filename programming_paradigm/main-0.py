# main-0.py

import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    parts = sys.argv[1].split(':', 1)
    command = parts[0]
    amount_str = parts[1] if len(parts) > 1 else None

    if command == "deposit" and amount_str is not None:
        try:
            amount = float(amount_str)
            account.deposit(amount)
            print(f"Deposited: ${amount:.2f}")
        except ValueError:
            print("Invalid amount for deposit.")
    elif command == "withdraw" and amount_str is not None:
        try:
            amount = float(amount_str)
            if account.withdraw(amount):
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
        except ValueError:
            print("Invalid amount for withdrawal.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()