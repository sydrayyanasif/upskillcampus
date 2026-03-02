class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance


    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid deposit amount.")


    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully.")
        else:
            print("Invalid or insufficient balance.")


    def display(self):
        print("\nAccount Holder:", self.name)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)




def main():
    print("=== Banking Information System ===")
    name = input("Enter account holder name: ")
    acc_no = input("Enter account number: ")
    account = BankAccount(name, acc_no)


    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Display Account Details")
        print("4. Exit")


        choice = input("Enter your choice: ")


        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            account.display()
        elif choice == '4':
            print("Thank you for using the Banking System.")
            break
        else:
            print("Invalid choice. Try again.")




if __name__ == "__main__":
    main()