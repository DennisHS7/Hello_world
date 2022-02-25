# 1

# import random
#
# a = [random.randint(0, 100) for i in range(10)]
# b = tuple(a)
# print(b)
# print('max', max(a), 'min', min(a))

# 2

# a = tuple([random.randint(0, 5) for _ in range(10)])
# b = tuple([random.randint(-5, 0) for _ in range(10)])
# c = a + b
# print(c, '\n Количество нулей: ', c.count(0))

# 3

# a = ('one', 'two', 'three')
# c = ','.join(a)
# print(c)
# print(a)

# 4

# A = (13, 5, 43, 49, 67, 32, 12, 98, 6, 10, 34, 20, 55, 68, 14, 60, 14)
# B = (53, 21, 4, 23, 76, 3, 43, 12, 54, 342, 21)
# s_A = sum(A)
# s_B = sum(B)
# if s_A > s_B:
#     print('Сумма больше в кортеже - А')
# else:
#     print('Сумма больше в кортеже - В')
#
# print('min A', min(A), 'Номер - ', A.index(min(A)))
# print('min B', min(B), 'Номер - ', B.index(min(B)))

# Закрепление темы.
#1

# a = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# b = sum(a)
# print(a)
# print(b)

#2

# long_word = ( 'т', 'т', 'а', 'и', 'и', 'а', 'и',
# 	         'и', 'и', 'т', 'т', 'а', 'и', 'и',
# 	         'и', 'и', 'и', 'т', 'и')
# print("Количество 'т':", long_word.count('т'))
# print("Количество 'и':", long_word.count('и'))
# print("Количество 'а':", long_word.count('а'))

# 3

# week_temp = (26, 29, 34, 32, 28, 26, 23)
# sum_temp = sum(week_temp)
# days = len(week_temp)
# mean_temp = int(sum_temp / days)
# print('week_temp: ',week_temp, '\nsum_temp: ', sum_temp,
#       '\ndays: ', days, '\nmean_temp: ', mean_temp)

# Homework

# 1 Найти самое длинное слово в строке.

# string = input("Enter a string: ")
#
# max_word = ''
# for word in string.split():
#     if len(word) > len(max_word):
#         max_word = word
#
# print(max_word)

# 2 Преобразовать текст в список слов с удалением знаков препинания.

# text = input('Enter text: ')
# symbols = '''!-;:'",.?'''
# no_symbol = ""
# for c in text:
#     if c not in symbols:
#         no_symbol = no_symbol + c
# print(no_symbol)

