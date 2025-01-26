'''
total = 0
for i in range(101):
    total += i
print(f'{total}')
'''

'''
total = 0
for i in range (2,101,2):
    if i % 2 == 0:
        total += i
print(f'{total}')
'''

total = 0
for i in range(1,16):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)