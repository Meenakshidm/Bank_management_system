class Bank():
    bank_name = "Bank of DHR"
    branch = "karlsruhe"

    def __init__(self, username, id, address):
        self.username = username
        self.id = id
        self.address = address
        self.balance = 0.0
        print(f'Hello {self.username} congratulations! you have created your account sucessfully')

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f'{amount} deposited sucessfully')

    def withdraw(self, amount):
        if amount<self.balance:
            self.balance = self.balance - amount
            print(f'you have withdrawn {amount} from your account')
        else:
            print("Insufficient fund")

    def account_statement(self):
        print(f'your account balance is {self.balance}')

print(f'welcome to {Bank.bank_name} {Bank.branch}')
username = input('Enter your name: ')
id = input('Enter your id: ')
address = input('Enter your address: ')

user = Bank(username, id, address)


while True:
    print("Please select the option: ")
    print("1.Deposit\n2.Withdraw\n3.Statement\n4Logout")
    option = int(input(" "))

    if option==1:
        amount = float(input("Please enter the amount to be deposited: "))
        user.deposit(amount)

    if option==2:
        amount = float(input("Enter the amount to be withdrawn: "))
        user.withdraw(amount)

    if option==3:
        user.account_statement()

    if option==4:
        print("You have successfully logged out")
        break



   

