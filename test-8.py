a = 0
n = int(input("Enter the target number: "))
while a < n:
    balance = (n - a)
    print(f"Balance Required {balance}")
    n2 = int(input("Enter a number: "))
    if n2 > balance:
        print("Number is too large!!")
        continue
    a = a + n2
print("Target Reached!")