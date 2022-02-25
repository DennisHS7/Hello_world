# 1

# even = 0
# odd = 0
# summa = 0
#
# a = input("Inter a seven-digit number: ")
#
# for i in a:
#     if int(i) % 2 == 0:
#         even += 1
#         summa += int(i)
#     else:
#         odd += 1
# print(summa if even > odd else int(a[0]) * int(a[2]) * int(a[4]))

# 2

# text = input(str("Enter text: "))
# cons = 0
# vowels = 0
# cons2 = []
# for i in text:
#     if i == 'e' or i == 'y' or i == 'u' or i == 'i' or i == 'o' or i == 'a':
#         vowels += 1
#         cons2 += i
#     else:
#         cons += 1
# print("vowels: ", vowels, "\nconsonants: ", cons)
# print(cons2 if cons == vowels else())

# 3

# import random

# a = int(input('Enter number 1(from 1 to 20): '))
# b = int(input('Enter number 2(from 1 to 20): '))
# i = 0
# rnd_dig = 0
# ent_dig = 0
# for i in range(7):
#     rnd_num1 = random.randint(1, 21)
#     rnd_num2 = random.randint(1, 21)
#     print(rnd_num1, rnd_num2)
#     if a + b >= rnd_num1 + rnd_num2:
#         ent_dig += 1
#     else:
#         rnd_dig += 1
# print("Введённые больше: ", ent_dig, "\nРандомных больше: ", rnd_dig )

# 4

# a = int(input("Количество введённых чисел: "))
# b = input("Число для поиска:")
# c1 = ''
# d = 0
# i = 0
# while i < a:
#     c = str(random.randint(1, 1000))
#     c1 += str(c) + ' '
#     i += 1
# print(c1)
# for e in str(c1):
#     if e == b:
#         d += 1
# print(d)

# 5

# a = input("Inter a string: ")
# dig = list(a)
# for i in dig:
#     if i.isdigit():
#         print(i, ' ', end='')

# 6

# word = input('Inter a word: ')
# pair_lower = 0
# pair_upper = 0
# for i in range(1, len(word)):
#     if word[i - 1].islower() and word[i].islower():
#         pair_lower += 1
#     if word[i - 1].isupper() and word[i].isupper():
#         pair_upper += 1
# print('letters in a word:', len(word), '\nupper case pairs:', pair_upper,
#       '\nlower case pairs:', pair_lower)
# print()
# cons = 0
# vowels = 0
# for i in word:
#     if i == 'e' or i == 'y' or i == 'u' or i == 'i' or i == 'o' or i == 'a':
#         vowels += 1
#     else:
#         cons += 1
# print('vowels: ', vowels,'\ncons: ', cons)

