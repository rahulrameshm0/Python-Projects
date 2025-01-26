class Bank:

    def __init__(self):
        self.users = {}
        self.current_user = None

    def is_user_found(self, user_name):
        if user_name in self.users:
           return True
        print("user is not found")
        return False
    def privilege(self):
        if self.current_user.privilege == "admin":
            return True

        print("You don't have privilege to access this account!")
        return False

    def list_user(self):
        if self.privilege():
            for index, (name,details) in enumerate(self.users.items(),start=1):
                print(f"{index}.Name: {name}, Balance: {details.balance}, Privilege: {details.privilege}")

    def create_account(self):
        if self.privilege():
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

    def delete_account(self):
        if self.privilege():
            delete_user = input("Enter the name of the user: ")
            if self.is_user_found(delete_user):
                self.users.pop(delete_user)
                print("account deleted successfully!")
                return

    def deposit(self, amount):
        self.current_user.balance += amount
        print(f"Deposited successfully!")

    def withdraw(self, amount):
        if amount > self.current_user.balance:
            print("your account balance is insufficient!")
            return False

        self.current_user.balance -= amount
        print(f"Withdrawn successfully!")
        return True

    def transfer(self):
        receiver_name = input("Enter the name of the receiver: ")
        if self.is_user_found(receiver_name):
            sending_amount = int(input("Enter the amount you need to sent: "))

            if self.withdraw(sending_amount):
                self.deposit(sending_amount)

    def menu(self):
        while True:
            try:
                print("Menu:\n(1)USER LIST\n(2)CHECK BALANCE\n(3)DEPOSIT\n(4)WITHDRAW\n(5)TRANSFER\n(6)ADD USER\n(7)REMOVE USER\n(8)LOGOUT")
                user_choice = int(input("Enter your choice: "))

                if user_choice == 1:
                    banking_system.list_user()

                elif user_choice == 2:
                    if self.current_user:
                       self.current_user.check_balance()

                elif user_choice == 3:
                    amount = int(input("Enter the amount: "))
                    banking_system.deposit(amount)

                elif user_choice == 4:
                    amount = int(input("Enter the amount: "))
                    banking_system.withdraw(amount)

                elif user_choice == 5:
                    banking_system.transfer()

                elif user_choice == 6:
                    banking_system.create_account()

                elif user_choice == 7:
                    banking_system.delete_account()

                elif user_choice == 8:
                    print("logout successfully!!")
                    break

                else:
                    print("Invalid option!!")

            except ValueError:
                print("Enter a valid input!")

    def login_user(self):
        while True:
            try:
                print("1.Login\n2.Exit")
                option = int(input("Enter your option: "))

                if option == 1:
                    username = input("Enter username: ")
                    password = input("Enter password: ")
                    if not banking_system.is_user_found(username) or banking_system.users[username].password != password:
                        print("username or password incorrect!")
                        continue
                    self.current_user = self.users[username]
                    self.menu()

                elif option == 2:
                    print("Thank You for using our banking system!")
                    exit()
                else:
                    print("Enter a valid input!")

            except ValueError:
                print("Enter a valid input!")

class User():
    def __init__(self, name, balance, password, privilege):
        self.name = name
        self.balance = balance
        self.password = password
        self.privilege = privilege

    def check_balance(self):
        print(f"Your account balance is {self.balance}")


banking_system = Bank()
banking_system.users["Rahul"] = User("Rahul", 25000, "7248", "admin")
banking_system.users["Jason"] = User("Jason", 6000, "8596", "user")
banking_system.users["Sonny"] = User("Sonny", 5500, "8748", "user")

banking_system.login_user()

# class Bank:
#
#     def __init__(self):
#         self.users = {}
#         self.current_user = None
#     def is_user_found(self,user_name):
#        return user_name in self.users
#
#     def privilege(self):
#         if self.current_user in self.users and self.users[self.current_user].privilege == "admin":
#             return True
#         print("You don't have privilege to access this account!")
#         return False
#
#     def list_user(self):
#         if self.privilege():
#             for index, (name,details) in enumerate(self.users.items(),start=1):
#                 print(f"{index}.Name: {name}, Balance: {details.balance}, Privilege: {details.privilege}")
#
#     def create_account(self):
#         if self.privilege():
#             add_user = input("Enter the name of the user: ")
#             if add_user in self.users:
#                 print("name exist!, please try with a different name!")
#                 return
#             amount = int(input("Deposit initial payment to start the account: "))
#             if amount < 5000:
#                 print("Amount should be 5000 or above!")
#                 return
#             create_password = input("Enter user password: ")
#
#             self.users[add_user] = User(add_user, amount, create_password, "user")
#             print("Account created successfully!")
#
#
#     def delete_account(self):
#         if self.privilege():
#             delete_user = input("Enter the name of the user: ")
#             if self.is_user_found(delete_user):
#                 del self.users[delete_user]
#                 print("account deleted successfully!")
#                 return
#
#     def deposit(self,amount):
#         banking_system.users[self.current_user].balance += amount
#         print(f"Amount has been successfully deposited into {self.current_user}'s account")
#
#     def withdraw(self,amount):
#         if amount > banking_system.users[self.current_user].balance:
#             print("your account balance is insufficient!")
#             return False
#
#         banking_system.users[self.current_user].balance -= amount
#         print(f"Amount withdrawn successfully from {self.current_user}'s account")
#         return True
#
#     def transfer(self):
#         receiver_name = input("Enter the name of the receiver: ")
#         if banking_system.is_user_found(receiver_name):
#             sending_amount = int(input("Enter the amount you need to sent: "))
#
#             if self.withdraw(sending_amount):
#                 self.deposit(sending_amount)
#
#     def login(self):
#         while True:
#             print("1.Login\n2.Exit")
#             option = int(input("Enter your option: "))
#
#             if option == 1:
#                 username = input("Enter username: ")
#                 password = input("Enter password: ")
#                 if not self.is_user_found(username) or self.users[username].password != password:
#                     print("username or password incorrect!")
#                     continue
#                 self.current_user = username
#                 print("login successful!")
#                 self.menu()
#             elif option == 2:
#                 print("Thank You for using our banking system!")
#                 exit()
#
#     def menu(self):
#         while True:
#             try:
#                 print("Menu:\n(1)USER LIST\n(2)CHECK BALANCE\n(3)DEPOSIT\n(4)WITHDRAW\n(5)TRANSFER\n(6)ADD USER\n(7)REMOVE USER\n(8)LOGOUT")
#                 user_choice = int(input("Enter your choice: "))
#
#                 if user_choice == 1:
#                     banking_system.list_user()
#
#                 elif user_choice == 2:
#                     if banking_system.current_user:
#                         current_user_object = self.users[self.current_user]
#                         current_user_object.check_balance()
#
#                 elif user_choice == 3:
#                     amount = int(input("Enter the amount: "))
#                     banking_system.deposit(amount)
#
#                 elif user_choice == 4:
#                     amount = int(input("Enter the amount: "))
#                     banking_system.withdraw(amount)
#
#                 elif user_choice == 5:
#                     banking_system.transfer()
#
#                 elif user_choice == 6:
#                     banking_system.create_account()
#
#                 elif user_choice == 7:
#                     banking_system.delete_account()
#
#                 elif user_choice == 8:
#                     print("logout successfully!!")
#                     break
#
#                 else:
#                     print("Invalid option!!")
#
#             except ValueError:
#                 print("Enter a valid input!")
#
# class User():
#     def __init__(self, name, balance, password, privilege):
#         self.name = name
#         self.balance = balance
#         self.password = password
#         self.privilege = privilege
#
#     def check_balance(self):
#         print(f"Your account balance is {banking_system.users[banking_system.current_user].balance}")
# banking_system = Bank()
# banking_system.users["Rahul"] = User("Rahul", 25000, "7248", "admin")
# banking_system.users["Jason"] = User("Jason", 6000, "8596", "user")
# banking_system.users["Sonny"] = User("Sonny", 5500, "8748", "user")
