def main():
    num_1 = int(input("Enter 1st number: "))
    num_2 = int(input("Enter 2nd number: "))

    print("1.ADD\n2.SUBTRACT\n3.MULTIPLY\n4.DIVIDE")
    user_choice = int(input("Enter your choice: "))
    calculator_creating(user_choice, num_1, num_2)
def calculator_creating(user_input,num1,num2):
    if user_input == 1:
        total = num1 + num2
        print(f"Result: {total}")
    elif user_input == 2:
        total = num1 - num2
        print(f"Result: {total}")
    elif user_input == 3:
        total = num1 * num2
        print(f"Result: {total}")
    elif user_input == 3:
        total = num1 / num2
        print(f"Result: {total}")

if __name__ == "__main__":
    main()