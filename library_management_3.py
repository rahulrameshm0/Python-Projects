class Library:
    def __init__(self):
        self.user_details = {}
        self.book_details = {}
        self.current_user = None
        self.borrowed_book = {}

    def privilege(self):
        if self.current_user.privilege == "admin":
            return True
        else:
            print("You have no privilege to access this section!")
            return False

    def is_book_found(self, book_name):
        if book_name in self.book_details:
            return True
        else:
            print(f"{book_name} is not available")
            return False

    def is_users_found(self, user_name):
        if user_name in self.user_details:
            return True
        print("User is not found!")
        return False
    def add_book(self):
        if self.privilege():
            book_name = input("Enter the name of the book: ")
            author_name = input("Enter the name of the author: ")
            book_count = int(input("Enter how many copy's of this book is available: "))
            self.book_details[book_name] = Book(book_name, author_name, book_count)
            print("book added successfully!")
    def remove_book(self):
        if self.privilege():
            remove_book = input("Enter the name of the book to remove: ")
            if self.is_book_found(remove_book):
                self.book_details.pop(remove_book)
                print("Book removed successfully")

    def borrow_book(self):
        book_name = input("Enter the name of the book: ")
        if self.is_book_found(book_name):
            book = self.book_details[book_name]
            if book_name in self.current_user.borrow_copy:
                print("You can only borrow 1 copy at time!")
                return
            if book.book_count > 0:
                if self.current_user.name not in self.borrowed_book:
                    self.borrowed_book[self.current_user.name] = []
                self.borrowed_book[self.current_user.name].append(book_name)
                self.current_user.borrow_copy.append(book_name)
                book.book_count -= 1
                print("book taken successfully!!")
            else:
                print("This book is not available now, please come back later.")

    def returns_book(self):
        return_books = input("Enter the name of the book: ")
        self.current_user.borrow_copy.remove(return_books)
        self.borrowed_book[self.current_user.name].remove(return_books)
        if not self.borrowed_book[self.current_user.name]:
            del self.borrowed_book[self.current_user.name]
        self.book_details[return_books].book_count += 1
        print(f"Book returned successfully")

    def filter_book(self):
        search_book = input("Enter the name or author name for the book: ")
        filter_book = [book for book in self.book_details.values() if search_book in book.book_name.lower() or search_book in book.author_name.lower()]

        if filter_book:
            for book in filter_book:
                print(f"Book name: {book.book_name}, Author name: {book.author_name}, Book copy's: {book.book_count}")
        else:
            print("There is no such book found!")

    def list_borrowed_book(self):
        if self.privilege():
            if self.borrowed_book:
                for (key, value) in self.borrowed_book.items():
                    print(f"- Book taken by: {key}, Name of book is: {value}")
            else:
                print("No one borrowed any book from the library!")


    def add_user(self):
        if self.privilege():
            username = input("Enter the name of the user: ")
            password = input("Create a password: ")
            contact = int(input("Enter the contact information: "))
            age = input("Enter the age: ")
            id_no = input("Enter the ID number: ")
            # total_book = int(input("Enter total book taken: "))
            self.user_details[username] = User(username, password, contact, id_no, age, "user", 1)
            print("user added successfully!")

    def delete_user(self):
        if self.privilege():
            remove_user = input("Enter the name of the user you need to remove: ")
            if self.is_users_found(remove_user):
                self.user_details.pop(remove_user)
                print("user has been deleted successfully: ")
    def list_users(self):
        if self.privilege():
            for user, details in self.user_details.items():
                print(f"- Name: {user}, Contact: {details.contact}, Privilege: {details.privilege}")

    def list_book(self):
        for (book, details) in self.book_details.items():
            print(f"- Name: {book}, Author: {details.author_name}")

    def update_user(self):

        old_name = input("Enter your current name: ")
        if self.is_users_found(old_name):
            user = self.user_details[old_name]
            update_name = input("Enter the new name: ")
            update_password = input("Enter new password: ")
            update_contact = int(input("Enter the new contact number: "))
            user.name = update_name,
            user.password = update_password,
            user.contact = update_contact
            print("User profile has updated successfully!")

            if update_name != old_name:
                self.user_details[update_name] = user
                del self.user_details[old_name]
                if self.current_user.name == update_name:
                    self.current_user = user

    def menu(self):
        while True:
            print("1.ADD BOOK\n2.DELETE BOOK\n3.BORROW BOOK\n4.RETURN BOOK\n5.SEARCH BOOK\n6.LIST BORROWED BOOK\n7.LIST AVAILABLE BOOK\n8.ADD USER\n9.DELETE USER\n10.LIST USER\n11.UPDATE USER\n12.LOGOUT")
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    self.add_book()
                elif choice == 2:
                    self.remove_book()
                elif choice == 3:
                    self.borrow_book()
                elif choice == 4:
                    self.returns_book()
                elif choice == 5:
                    self.filter_book()
                elif choice == 6:
                    self.list_borrowed_book()
                elif choice == 7:
                    self.list_book()
                elif choice == 8:
                    self.add_user()
                elif choice == 9:
                    self.delete_user()
                elif choice == 10:
                    self.list_users()
                elif choice == 11:
                    self.update_user()
                elif choice == 12:
                    self.log_in()
                    exit()
                else:
                    print("Enter a valid option!")
                    continue

            except ValueError:
                print("Enter a valid input")
    def log_in(self):
        while True:
            print("1.Login\n2.Exit")
            try:
                option = int(input("Enter your option: "))
                if option == 1:
                    username = input("username: ")
                    password = input("password: ")

                    if username not in self.user_details or self.user_details[username].password != password:
                        print("username or password is incorrect!")
                        continue
                    else:
                        self.current_user = self.user_details[username]
                        self.menu()

                elif option == 2:
                    print("Thank You for using our banking system!")
                    break

                else:
                    print('provide a valid number!')

            except ValueError:
                print("Please enter a valid input!")
class Book:
    def __init__(self, book_name, author_name, book_count):
        self.book_name = book_name
        self.author_name = author_name
        self.book_count = book_count

class User:

    def __init__(self, name, password, contact, id_no, age, privilege, user_count):
        self.name = name
        self.password = password
        self.contact = contact
        self.id_no = id_no
        self.age = age
        self.privilege = privilege
        self.user_count = user_count
        self.borrow_limit = 1
        self.borrow_copy = []

def main():
    library_management = Library()

    library_management.book_details["b"] = Book("b", "JK", 5)
    library_books = Book("Harry 2", "Jk", 3)

    library_management.user_details["Rahul"] = User("Rahul", "7248", 9496320858, 1, 26, "admin",1)
    library_management.user_details["a"] = User("a", "2580", 9036520858, 2, 27, "user",1)

    library_user = User("default","","","","","", "")

    print("Welcome to library management system!")
    library_management.log_in()

if __name__ == "__main__":
    main()