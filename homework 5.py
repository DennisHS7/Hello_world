# 1

i = 1
while i <= 10:
    print(i ** 2)
    i += 1

# 2

i = 1
result = 0
while i <= 9435:
    if i % 2 == 0:
        result = i * i
    i += 1
print(result)

# 3

i = 15
while i != 0:
    print(i)
    i -= 1

# 4

a = int(input("Inter the firsr number: "))
b = int(input("Inter the second number: "))

while a < b:
    a += 1
    if a == 0:
        break
    print(a)

# 5

a = 0
mas = []
while a < 98:
    a += 7
    mas.append(a)

print(mas, 'Длинна: ', len(mas))

# 6

print("Ноль, в качестве знака операции, завершит программу!")
x = float(input("x= "))
y = float(input("y= "))
while True:
    s = input("Знак (+,-,*,/): ")
    if s == '0':
        break
    elif s == '+':
        print(x+y)
    elif s == '-':
        print(x-y)
    elif s == '*':
        print(x*y)
    elif s == '/':
        if y != 0:
            print(x/y)
        else:
            print("Деление на ноль!")

# 7

i = ["1, 2, 3, 4, 5, 6, 7"]
sum = 1
pr = 1
while i:

# Homework

import random
i = 0
while i < 5:
    colorseq = ['red', 'black']
    a = random.randint(1, 10)
    b = random.choice(colorseq)
    result1 = (str(a) + " " + b)

    c = int(input("Select a number from 1 to 10: "))
    d = str(input("Choose color 'red' or 'black': "))
    result2 = (str(c) + " " + d)
    if result1 == result2:
        print("you win")
        break
    else:
        print("try again")
        i += 1
else:
    print("you lose")

