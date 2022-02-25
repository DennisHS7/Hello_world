# 1 Дан произвольный список.
# Представить его в обратном порядке.

# arbitrary_list = [1, 2, 3, 4, 5]
# print(arbitrary_list[::-1])
#
# arbitrary_list = [1, 2, 3, 4, 5]
# arbitrary_list.reverse()
# print(arbitrary_list)

# 2 Дан список некоторых целых чисел, найдите значение 20 в нем и, если оно присутствует,
# замените его на 200. Обновите список только при первом вхождении числа 20.

# list1 = [5, 10, 20, 30, 20, 56, 78, 20]
#
# print("Список: \n, list1")
#
# ind = list1.index(20)
# list1[ind] = 200
#
# print("Изменённый список: \n, list1")

# 3 Список из 7 цифр. Если четных цифр в нем больше чем нечетных,
# то найти сумму всех его цифр, если нечетных больше, то найти произведение 1 3 и 6 элемента.

# mas = [2, 3, 4, 5, 6, 7, 8, ]
# count = 0
# count_2 = 0
# for i in mas:
#     if i % 2 == 0:
#         count += 1
#     else:
#         count_2 += 1
# print("Чётных: ", count, "Нечётных: ", count_2)
# sum = 0
# pr = 1
# if count > count_2:
#     for i in mas:
#         sum += 1
#     print("Сумма: ", sum)
# else:
#     pr = mas[0] * mas[2] * mas[5]
#     print("Произведение: ", pr)

# 4 Найти совпадающие элементы двух списков.
# Эти значения записать в новый список

# a = [5, [1, 2], 2, 'r', 4, 'ee']
# b = [4, 'we', 'ee', 3, [1, 2]]
# c = []
# for i in a:
#     if i in b:
#         c.append(i)
# print(c)

# 5 1.Сложить два списка
#   2.Добавьте элемент 6 на 3 позицию
#   3.Удалите все текстовые переменные
#   4.Посчитайте количество элементов списка

# a = [4, 6, 'pу', 'tell', 78]
# b = [44, 'hello', 56, 'exept', 3]
#
# a.extend(b)
# a.insert(3, 6)
# print(a)
# for i in a:
#     if type(i) is str:
#         a.remove(i)
# a.sort()
# print(a)

# Homework 1.Все числа этого списка проверить на чётность.
# Если число чётное, то посчитать сумму его цифр.
# 2.Если нечётное, то заменить  его на 1 в списке.
# 3.Все слова: посчитать количество гласных и согласных.
# 4.Вывести всё на экран.

list1 = ['15', '48', 'hello', '12', '19', 'world']

print(list1)

sum_even_number = 0

for item in range(len(list1)):
    if list1[item].isdigit() and int(list1[item]) % 2 == 0:
        for i in range(len(list1[item])):
            sum_even_number += int(list1[item][i])
        print(f"sum digits of {list1[item]}: {sum_even_number}")
        sum_even_number = 0
    elif list1[item].isdigit() and int(item) % 2 != 0:
        list1[item] = '1'

print(list1)

