class School:
    def __init__(self):
        self.student_details = {}
        self.current_user = None
        self.admin_details = {}

    def privilege(self):
        if self.current_user.privilege == "admin":
            return True
        print("you have no access to this section!")
        return False

    def add_student(self):
        if self.privilege():
            name = input('Enter the name of the student: ')
            age = int(input("Enter the age of the student: "))
            course = input("Enter the course name of the student: ")
            self.student_details = {
                "name": name,
                "age": age,
                "course": course
            }
            print("Student details added successfully!")

    def delete_student(self):
        pass

    def login(self):
        while True:
            print("1.login\n2.Exit")
            try:
                option = int(input("Enter your option: "))
                if option == 1:
                    login = input('Enter the username: ')
                    password = input("Enter your password: ")
                    if login not in self.admin_details or self.admin_details[login].password != password:
                        print("user name or password is incorrect!")
                    else:
                        self.current_user = self.admin_details[login]
                        self.menu()
                elif option == 2:
                    print("Thank you for banking system!")
                    exit()

            except ValueError:
                print("Please enter a valid number!")


    def menu(self):
        while True:
            try:
                print("1.ADD STUDENT\n2.DELETE STUDENT\n3.UPDATE STUDENT ADDRESS\n4.LIST ALL STUDENT")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    self.add_student()
                elif choice == 2:
                    self.delete_student()
            except ValueError:
                print('Please enter a valid input!')
                continue
class Student_Details:
    def __init__(self, names, grade, age, roll_no):
        self.name = names
        self.grade = grade
        self.age = age
        self.roll_no = roll_no

class Principal:
    def __init__(self, names, privilege, password):
        self.name = names
        self.privilege = privilege
        self.password = password
def main():
    student = School()
    student.admin_details["John"] = Principal("John", "admin","7248")
    student.student_details["Rahul"] = Student_Details("Rahul",35,14,1)
    student.login()
if __name__ == "__main__":
    main()