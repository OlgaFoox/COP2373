class BankAcct:
    def __init__(self, name, account_number, amount, interest_rate):
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate  # Annual interest rate in decimal form (e.g., 0.05 for 5%)
    
    def adjust_interest_rate(self, new_rate):
        """Adjust the interest rate to the new rate."""
        self.interest_rate = new_rate
    
    def deposit(self, amount):
        """Deposit money into the account."""
        self.amount += amount
        return self.amount
    
    def withdraw(self, amount):
        """Withdraw money from the account if sufficient funds exist."""
        if amount > self.amount:
            print("Insufficient funds")
        else:
            self.amount -= amount
        return self.amount
    
    def balance(self):
        """Return the current balance of the account."""
        return self.amount
    
    def calculate_interest(self, days):
        """Calculates interest earned over a given number of days."""
        daily_interest_rate = self.interest_rate / 365
        interest = self.amount * daily_interest_rate * days
        return interest
    
    def __str__(self):
        """Return a string representation of the account balance and interest rate."""
        return f"Account Name: {self.name}, Account Number: {self.account_number}, Balance: ${self.amount:.2f}, Interest Rate: {self.interest_rate*100:.2f}%"

def test_bank_acct():
    """Test function to demonstrate the functionality of the BankAcct class."""
    # Create a new bank account
    account = BankAcct("John Doe", "123456789", 1000.00, 0.05)
    
    print(account)  # Display account information
    
    # Deposit money
    print("Depositing $500...")
    account.deposit(500)
    print(account)
    
    # Withdraw money
    print("Withdrawing $200...")
    account.withdraw(200)
    print(account)
    
    # Attempt to withdraw more than the balance
    print("Withdrawing $2000...")
    account.withdraw(2000)
    
    # Adjust interest rate
    print("Adjusting interest rate to 3%...")
    account.adjust_interest_rate(0.03)
    print(account)
    
    # Calculate interest for 30 days
    interest = account.calculate_interest(30)
    print(f"Interest earned over 30 days: ${interest:.2f}")

if __name__ == "__main__":
    test_bank_acct()
