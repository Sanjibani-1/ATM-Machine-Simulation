class ATM:
    def __init__(self, initial_pin=1234):
        """
        Initialize the ATM with a default balance and an initial PIN.
        """
        self.balance = 0.0  # Initial balance is set to zero
        self.pin = initial_pin  # Default PIN is 1234
        self.transaction_history = []  # List to store transaction history

    def authenticate(self):
        """
        Authenticate the user by asking for their PIN.
        """
        entered_pin = int(input("Enter your PIN: "))
        if entered_pin == self.pin:
            return True
        else:
            print("Incorrect PIN. Please try again.")
            return False

    def check_balance(self):
        """
        Display the current account balance.
        """
        print(f"Your current balance is: ${self.balance:.2f}")
        self.transaction_history.append("Checked balance")

    def deposit(self, amount):
        """
        Deposit a specified amount into the account.
        """
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} deposited successfully.")
            self.transaction_history.append(f"Deposited ${amount:.2f}")
        else:
            print("Invalid amount. Please enter a positive value.")

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the account.
        """
        if amount <= 0:
            print("Invalid amount. Please enter a positive value.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"${amount:.2f} withdrawn successfully.")
            self.transaction_history.append(f"Withdrew ${amount:.2f}")

    def change_pin(self):
        """
        Change the PIN after authenticating the current one.
        """
        if self.authenticate():
            new_pin = int(input("Enter new PIN: "))
            confirm_pin = int(input("Confirm new PIN: "))
            if new_pin == confirm_pin:
                self.pin = new_pin
                print("PIN changed successfully.")
                self.transaction_history.append("Changed PIN")
            else:
                print("PIN mismatch. Please try again.")

    def show_transaction_history(self):
        """
        Display the transaction history.
        """
        if not self.transaction_history:
            print("No transactions found.")
        else:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(f"- {transaction}")

    def start(self):
        """
        Start the ATM program, displaying options for user interaction.
        """
        print("Welcome to the ATM Machine!")

        if not self.authenticate():
            return

        while True:
            print("\nPlease select an option:")
            print("1. Check Balance")
            print("2. Deposit Cash")
            print("3. Withdraw Cash")
            print("4. Change PIN")
            print("5. Transaction History")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.check_balance()
            elif choice == '2':
                amount = float(input("Enter amount to deposit: "))
                self.deposit(amount)
            elif choice == '3':
                amount = float(input("Enter amount to withdraw: "))
                self.withdraw(amount)
            elif choice == '4':
                self.change_pin()
            elif choice == '5':
                self.show_transaction_history()
            elif choice == '6':
                print("Thank you for using the ATM Machine. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Instantiate the ATM class and start the ATM machine
atm = ATM()
atm.start()
