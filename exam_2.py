# 1

# list_1 = [1, 4, 5,  2, 2, 3, 1, 2, 5, 8]
# list_1_2 = []
# for i in list_1:
#     if list_1.count(i) == 1:
#         list_1_2.append(i)
# print(list_1_2)

# 2

# list_2 = [1, 1, 2, 3, 5, 5, 11, 8, 11, 6, 11]
# pare = 0
# for i in range(len(list_2)):
#     for j in range(i + 1):
#         if list_2[i] == list_2[j]:
#             pare += 1
# print(pare)


# 3

# C_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
# C_2 = (45, 21, 124, 76, 5, 23, 91, 234)
# s1 = sum(C_1)
# s2 = sum(C_2)
# if s1 > s2:
#     print('Сумма больше в кортеже: C_1')
# else:
#     print('Сумма больше в кортеже: C_2')
# print('Numb min elem tup C_1: ',C_1.index(min(C_1)), 'Numb max elem tup C_1: ',C_1.index(max(C_1)))
# print('Numb min elem tup C_2: ',C_2.index(min(C_2)), 'Numb max elem tup C_2: ',C_2.index(max(C_2)))

# 4

# a = 'An apple a day keeps the doctor away'
# dicta = {i: a.count(i) for i in a}
# print(dicta)

# 6

# list3 = [1, 2, 2, 3, 5, 3, 6, 3, 3, 3, 3, 5, 6, 1]
# list4 = [2, 3, 5, 9, 6, 3, 1]
# digs = 0
#
# for i in range(len(list3)):
#     if i in list4:
#         digs += 1
# print(digs)

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