class Bank:

    def __init__(self):
        self.users = {}
    def is_user_found(self,user_name):
       return user_name in self.users

    def privilege(self,username):
        if username in self.users and self.users[username].privilege == "admin":
            return True
        print("You don't have privilege to access this account!")
        return False

    def list_user(self,username):
        if self.privilege(username):
            for index, (name,details) in enumerate(self.users.items(),start=1):
                print(f"{index}.Name: {name}, Balance: {details.balance}, Privilege: {details.privilege}")

    def create_account(self,admin_username):
        if self.privilege(admin_username):
            add_user = input("Enter the name of the user: ")
            if add_user in self.users:
                print("name exist!, please try with a different name!")
                return
            amount = int(input("Deposit initial payment to start the account: "))
            if amount < 5000:
                print("Amount should be 5000 or above!")
                return
            create_password = input("Enter user password: ")

            self.users[add_user] = User(add_user, amount, create_password, "user")
            print("Account created successfully!")


    def delete_account(self,admin_username):
        if self.privilege(admin_username):
            delete_user = input("Enter the name of the user: ")
            if self.is_user_found(delete_user):
                self.users.pop(delete_user)
                print("account deleted successfully!")
                return

    def deposit(self, username, amount):
        banking_system.users[username].balance += amount
        print(f"Amount has been successfully deposited into {username}'s account")

    def withdraw(self, username, amount):
        if amount > banking_system.users[username].balance:
            print("your account balance is insufficient!")
            return False

        banking_system.users[username].balance -= amount
        print(f"Amount withdrawn successfully from {username}'s account")
        return True

    def transfer(self, username):
        receiver_name = input("Enter the name of the receiver: ")
        if banking_system.is_user_found(receiver_name):
            sending_amount = int(input("Enter the amount you need to sent: "))

            if self.withdraw(username, sending_amount):
                self.deposit(receiver_name, sending_amount)

class User():
    def __init__(self, name, balance, password, privilege):
        self.name = name
        self.balance = balance
        self.password = password
        self.privilege = privilege

    def check_balance(self, username):
        print(f"Your account balance is {banking_system.users[username].balance}")

def user_option(banking_system):
    while True:
        print("1.Login\n2.Exit")
        option = int(input("Enter your option: "))

        if option == 1:
            username = input("Enter username: ")
            password = input("Enter password: ")
            if not banking_system.is_user_found(username) or banking_system.users[username].password != password:
                print("username or password incorrect!")
                continue

            while True:
                try:
                    print("Menu:\n(1)USER LIST\n(2)CHECK BALANCE\n(3)DEPOSIT\n(4)WITHDRAW\n(5)TRANSFER\n(6)ADD USER\n(7)REMOVE USER\n(8)LOGOUT")
                    user_choice = int(input("Enter your choice: "))

                    if user_choice == 1:
                        banking_system.list_user(username)

                    elif user_choice == 2:
                        banking_system.users[username].check_balance(username)

                    elif user_choice == 3:
                        amount = int(input("Enter the amount: "))
                        banking_system.deposit(username, amount)

                    elif user_choice == 4:
                        amount = int(input("Enter the amount: "))
                        banking_system.withdraw(username, amount)

                    elif user_choice == 5:
                        banking_system.transfer(username)

                    elif user_choice == 6:
                        banking_system.create_account(username)

                    elif user_choice == 7:
                        banking_system.delete_account(username)

                    elif user_choice == 8:
                        print("logout successfully!!")
                        break

                    else:
                        print("Invalid option!!")

                except ValueError:
                    print("Enter a valid input!")
        elif option == 2:
            print("Thank You for using our banking system!")
            exit()

banking_system = Bank()
banking_system.users["Rahul"] = User("Rahul", 25000, "7248", "admin")
banking_system.users["Jason"] = User("Jason", 6000, "8596", "user")
banking_system.users["Sonny"] = User("Sonny", 5500, "8748", "user")
user_option(banking_system)