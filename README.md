# ATM-Machine-Simulation
# Explanation
ATM Class Initialization (__init__):

Initializes balance, sets a default PIN, and prepares an empty transaction history.
Authentication (authenticate):

Checks the PIN entered by the user before allowing access to certain features.
Check Balance (check_balance):

Prints the current balance and logs this action in the transaction history.
Deposit (deposit):

Increases the balance by the amount entered and logs the transaction if the amount is valid.
Withdraw (withdraw):

Checks if the withdrawal amount is valid and sufficient, then decreases the balance accordingly and logs the transaction.
Change PIN (change_pin):

Authenticates the user, allows them to set a new PIN after confirming it, and logs the change.
Transaction History (show_transaction_history):

Displays all actions performed during the session, including deposits, withdrawals, and balance inquiries.
Main Loop (start):

Displays menu options, takes user input, and calls the relevant methods until the user decides to exit.
This simulation covers the essential functions of a basic ATM interface, with user authentication and transaction tracking.
