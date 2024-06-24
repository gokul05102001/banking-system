class BankSystem:
    def __init__(self):
        self.accounts = {}
    def create_account(self, username, password):
        if username in self.accounts:
            print("Account already exists")
        else:
            self.accounts[username] = {'password': password, 'balance': 0}
            print("Account created successfully")
    def login(self, username, password):
        if username in self.accounts and self.accounts[username]['password'] == password:
            print("Login successful!")
            return True
        else:
            print("Invalid username or password")
            return False
    def deposit(self, username, amount):
        if amount > 0:
            self.accounts[username]['balance'] += amount
            print(f"Deposited {amount}. New balance: {self.accounts[username]['balance']}")
        else:
            print("Amount must be greater than 0")
    def withdraw(self, username, amount):
        if amount > 0:
            if self.accounts[username]['balance'] >= amount:
                self.accounts[username]['balance'] -= amount
                print(f"Withdrew {amount}. New balance: {self.accounts[username]['balance']}")
            else:
                print("Insufficient funds")
        else:
            print("Amount must be greater than 0")

def main():
    bank = BankSystem()

    while True:
        print("\nBanking System Menu:\n1. Create Account\n2. Login\n3. Deposit\n4. Withdraw\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            bank.create_account(username, password)
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if bank.login(username, password):
                print("Logged in successfully")
            else:
                print("Login failed.")
        elif choice == '3':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if bank.login(username, password):
                amount = float(input("Enter amount to deposit:"))
                bank.deposit(username, amount)
        elif choice == '4':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if bank.login(username, password):
                amount = float(input("Enter amount to withdraw: "))
                bank.withdraw(username, amount)
        elif choice == '5':
            print("Exiting")
            break
        else:
            print("Invalid choice, please try again")

if __name__ == "__main__":
    main()
