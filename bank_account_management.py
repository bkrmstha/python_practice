class BankAccount:
    
    def __init__(self, account_number, account_holder_name, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance
        
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
        else:
            self.balance += amount
            print("Deposit Successful.")
            print(f"Deposited amount: {amount}")
            self.check_balance()
            
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print("Withdrawal successful.")
            print(f"Withdrawn amount: {amount}")
            self.check_balance()
            
    def check_balance(self):
        print(f"Current Balance: {self.balance}")
        
    def display_info(self):
        print("Bank Account Details: ")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder_name}")
        print(f"Balance: {self.balance}")
        
account1 = BankAccount(1001, "Bikram Shrestha", 15000)
account2 = BankAccount(1002, "Diya Shrestha", 20000)
account3 = BankAccount(1003, "Suprem Giri", 10000)

accounts = {
    1001 : account1,
    1002 : account2,
    1003 : account3
    }

while True:
    print("Bank Account Management:")
    print("1. Select Account")
    print("2. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Available Accounts:")
        for account_number, account in accounts.items():
            print(account_number, "-", account.account_holder_name)
            
        acc_no = int(input("Enter account number: "))
        
        if acc_no in accounts:
            selected_account = accounts[acc_no]
            
            while True:
                print("\nAccount Menu: ")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Account Information")
                print("5. Back to Main Menu")
                
                option = int(input("Enter your choice: "))
                if option == 1:
                    amount = float(input("Enter deposit amount: "))
                    selected_account.deposit(amount)
                    
                elif option == 2:
                    amount = float(input("Enter withdrawal amount: "))
                    selected_account.withdraw(amount)
                    
                elif option == 3:
                    selected_account.check_balance()
                    
                elif option == 4:
                    selected_account.display_info()
                    
                elif option == 5:
                    break
                
                else:
                    print("Invalid choice!")
                    
        else:
            print("Account not found!")
            
    elif choice == 2:
        print("Banking System Exited!")
        break
    
    else:
        print("Invalid Choice!")