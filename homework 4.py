# Exercise 1
a = input('Inter the string: ')
b = input('Inter character: ')
c = ''
for i in a:
    if i != b:
        c += i
print('Result: ', c)

# Exercise 2
a = int(input('Enter start: '))
b = int(input('Enter end: '))
c = int(input('Enter step: '))
for i in range(a, b, c):
    print(i)

#Exercise 3
for i in range(54, 9184, 1):
     if i % 5 == 0:
         print(i)

# Exercise 4
food = ["макароны", "пельмени", "печень", "яйца"]
a = input("ведите блюдо: ")
for i in food:
    if i == a:
        print("Я не ем " + a)
        break
    print("Вкусные " + i)

# Exercise 5
arr = [1, 2, 3, 4, 5, 6, 7, 8]
sum = 0
pr = 1
for i in arr:
    sum += i
    pr *= i
print("Сумма", sum)
print("Сумма", pr)

# Exercise 6
for i in range(1,10):
    for j in range(1,10):
        print(i*j, '', end='')
    print()

#Homework
#1
pr = 1
for i in range(1,100,2):
    pr *= i
print('Произведение', pr)
#2
print([i for i in range(1,500,1) if i % 5 == 0])
#3
for i in range(1,497):
    if i % 2 == 0:
        print(i)
#4
arr = [2, 3, 4, 4, 5, 6, 99, 99, 99, 1, 1, 1]
arr1 =[]
for i in arr:
    if arr.count(i) > 2:
        arr1.append(i)
print(arr)
print(arr1)