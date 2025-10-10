import sys
from bank_account import BankAccount

def main():
    account = BankAccount(50.0)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <deposit|withdraw|balance> [amount]")
        sys.exit(1)

    command, *params = sys.argv[1].lower() 
    amount = float(sys.argv[2]) if len(sys.argv) > 2 else 0.0

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print(f"Insfficient funds")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()