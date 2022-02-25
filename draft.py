# default_list = []
#
# sum_even_number = 0
#
# # User interface
# user_input = input("enter  words, numbers(integer, float), boolean: \n")
#
# # business logic
# default_list.extend(user_input.split())
#
#
# for item in range(len(default_list)):
#     if default_list[item].isdigit() and int(default_list[item]) % 2 == 0:
#         for i in range(len(default_list[item])):
#             sum_even_number += int(default_list[item][i])
#         print(f"sum digits of {default_list[item]}: {sum_even_number}")
#         sum_even_number = 0
#     elif default_list[item].isdigit() and int(item) % 2 != 0:
#         default_list[item] = '1'
#
# # UI
# print(default_list)

# number = 23456
#
# summer = 0
#
# while number != 0:
#     summer += number % 10
#     number //= 10
#
# print(summer)
#
# summer = 0
# number = 23456
#
# number = str(number)
# for i in number:
#     summer += int(i)
#
# print(summer)

# -----------------------------------------------------

# string = "word23ho34nnor)(*gerg&&%^*&9846"
#
# string_number = ''
# string_digit = ''
# string_other = ''
#
# for i in string:
#     if i.isalpha():
#         string_number += i
#     elif i.isdigit():
#         string_digit += i
#     else:
#         string_other += i
#
# print(f"{string_digit = }, {string_number = }, {string_other = }")

# ---------------------------------------------------------------
# import random
#
# # id, name, birthday, gender
#
# names = ("Artur", "Olga", "Denis", "Svetlana", "Inna", "Ivan", "Dmitry")
#
# database = []
# user_id = 0
# user_name = ''
# birthday = ''
# gender = 0
#
# msg = ''

# UI
# for i in range(7):
#     user_id = random.randint(1, 100)
#     user_name = names[random.randint(0, len(names) - 1)]
#     birthdate = (str(random.randint(1, 32)), str(random.randint(1, 13)), str(random.randint(1923, 2020)))
#     birthday = "-".join(birthdate)
#     gender = 1 if user_name[-1] == 'a' else 0
#
#     database.append((user_id, user_name, birthday, gender))

# msg = f"{user_id = }, {user_name = }, {birthday = }, {gender = }"

# for user in database:
#     print(user)
#
# string = "this is string without register"
#
# new_string = ""
#
# list_string = string.split()
# print(list_string)
#
# camelcase_list = []
# new_word = ""
#
# for word in list_string:
#     for letter in range(len(word)):
#         if letter % 2 == 0:
#             new_word += word[letter].upper()
#         else:
#             new_word += word[letter].lower()
#     camelcase_list.append(new_word)
#     new_word = ""
#
# new_string = ' '.join(camelcase_list)
#
# print(new_string)

# ------------------------------------------------

# number = int(input("enter number: "))
#
# i = 2
# msg = ""
# prime = False
#
# for i in range(number // 2):
#     if number % i == 0:
#         prime = False
#         break
#     i += 1
#
# msg = "prime" if prime else "not prime"
#
# print(msg)

# --------------------------------------------

# word = ""
# user_enter = input("letter: ")
# while user_enter != "":
#     if 'a' <= user_enter <= 'z' and user_enter in "aueoi":
#         word += user_enter
#     user_enter = input("letter: ")
#
# print(word)

# for user in database:
#     for data in range(len(user)):
#         bd = user[2].split('-')
#         if int(bd[2]) < 2004:
#             print(user)
#             break
#
# digits = [random.randint(0, 999) for i in range(20)]
# print(digits)
#
# for i in digits:
#     if len(str(i)) >= 3:
#         print(i, end=" ")
#
# print(f"\nmin = {min(digits)}, max = {max(digits)}")
#
# print(ord('t'))
#
# expretion = input(": ")
# print(eval(expretion))
# Кортежи tuple
# a = (1, 2, 3, 4, 5, 5)
# print(a.count(5), len(a))

# x = (1, 2, 3, 4)
# y = (5, 6, 7, 8)
# z = x + y
# print(z)

# a = ('one', 'two', 'three')
# c = ','.join(a)
# print(c)
# print(a)

# long_word = ( 'т', 'т', 'а', 'и', 'и', 'а', 'и',
# 	         'и', 'и', 'т', 'т', 'а', 'и', 'и',
# 	         'и', 'и', 'и', 'т', 'и')
# print("Количество 'т':", long_word.count('т'))
# print("Количество 'и':", long_word.count('и'))
# print("Количество 'а':", long_word.count('а'))

# text = input('Enter text: ')
# pair_lower = 0
# pair_upper = 0
# for i in range(1, len(text)):
#     if text[i - 1].islower() and text[i].islower():
#         pair_lower += 1
#     if text[i - 1].isupper() and text[i].isupper():
#         pair_upper += 1
# print('upper case pairs:', pair_upper)
# print('lower case pairs:', pair_lower)

# import random
# num_count = int(input("Enter quantity numbers: "))
# dig = (input("Enter found digit: "))
# num_string = ''
# count = 0
# i = 0
# while i < num_count:
#     num = random.randrange(1, 1000)
#     num_string += str(num) + ' '
#     i += 1
# print(num_string)
# for j in num_string:
#     if j == dig:
#         count += 1
# print(count)
# print("____________________________________\n")

N = 4
M = 2
A = [[2] * M for i in range(N)]
print(A)

