print("Welcome to budget tracker!")
amount = 0
total_spent = 0
shopping = {}

user_input = int(input("Enter your initial budget: "))
amount += user_input


while True:
    try:
        print("What would you like to do?\n1.Add an expense\n2.Show budget details\n3.Exit")
        user_choice = int(input("Enter your choice: "))

        if user_choice == 1:
            description = input("Enter expense description: ")
            expense_amount = int(input("Enter the expense: "))
            if expense_amount > user_input:
                print("Insufficient fund!")
                continue
            shopping[description] = expense_amount
            print(f"Added expense: {description}, amount: {expense_amount}")
        elif user_choice == 2:
            print(f"Total budget: {amount}")
            print(f"Expense:")
            for key, value in shopping.items():
                print(f"- {key}: {value}")
                total_spent += value
            print(f"Total spent: {total_spent}")
            print(f"Balance remaining: {amount - total_spent}")
        elif user_choice == 3:
            print("Thank you for using budget tracking!")
            break
        else:
            print("Enter a valid number!")
    except ValueError:
        print("Enter a valid input!")