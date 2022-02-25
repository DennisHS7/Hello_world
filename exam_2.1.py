# 6

# list3 = [1, 2, 2, 3, 5, 3, 6, 3]
# list4 = [2, 3, 5, 9, 6, 3, 1]
# digs = 0
#
# for i in range(len(list3)):
#     if i in list4:
#         digs += 1
# print(digs)

# 4

# a = 'An apple a day keeps the doctor away'
# dicta = {i: a.count(i) for i in a}
# print(dicta)

# 7

# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter the second number: "))
#     print("Division result: ", num1 / num2)
# except ValueError:
#     print("Преобразование прошло не удачно")
# except ZeroDivisionError:
#     print("Попытка деления на ноль")
# except Exception:
#     print("Общее исключение")
# finally:
#     print("Программа завершена")

# 8

# f = open(input("File: "), 'w+')
# while True:
#     name = input('First Name Last Name: ')
#     grade = input('Control score: ')
#     f.write(str(dict(zip(name, grade))) + '\n')
#     if name == '':
#         f.close()
#         break
f = open('Clas_9B.txt', 'r')
print(f.readlines())
a = {}
for

# 5

# confectionery = {"Торт": ['бисквит, крем, коньяк', 2, 3000],
#                  "Пирожное": ['мука, орехи, изюм', 3, 2000],
#                  "Маффин": ['масло, молоко, мука', 4, 1000]}
# while True:
#     print(confectionery)
#     print('1-Описание', '2-Цена', '3-Количество', '4-Весь ассортимент',
#           '5-Приступить к покупке', '" " - выход из программы')
#     a = input("Здравструйте, что желаете: ")
#     if a == " ":
#         break
#     if a == 1:
#         print()

