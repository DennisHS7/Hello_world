
# with open("file1.txt") as f:
#     s = f.readlines()
#     print(s)
# for i in s:
#     i = i.replace('_', ' ')
#     l = i.split(' ')
# print(l)
# summer = 0
# for i in l:
#     if i.isdigit():
#         summer += int(i)
# print(summer)

# f = open('file_2.txt')
# word = []
# dig = []
# s = f.readlines()
# print(s)
# for i in s:
#     i = i[:-1]
#     if i.isalpha():
#         i = str(i)
#         word.append(i)
#     elif i.isdigit():
#         i = int(i)
#         dig.append(i)
# print(dig)
# print(word)
# dig.sort()
# word.sort()
# mas = dig + word
# print(mas)

# bobber = input('Файл: ')
# f = open(bobber, 'w')
# while True:
#     s = input()
#     if s == '':
#         break
#     f.write(s + '\n')
# f.close()

# f = open('file_3')
# line = 0
# for i in f:
#     line += 1
#     print(i, len(i), 'symb.')
# print(line, 'str.')
# f.close()


array = ['1', '2', '568', '11', 'qwe', 'asds', 'f', 'hj']
digits = []
words = []

for i in array:
    if i.isdigit():
        digits.append(i)
    if i.isalpha():
        words.append(i)
words.sort(key=len)     # По длинне слов
digits.sort(key=len)    # В порядке возростания
obd = words + digits
obd = ' '.join(obd)
print(obd)

with open('file_4.txt,', 'w') as file:
    file.write(obd)



