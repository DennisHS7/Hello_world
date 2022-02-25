from random import randint
a = randint(100, 999)
print(a)
b = a //100
c = (a // 10) % 10
d = a % 10
print(b + c + d)

from random import random
x = random() * 900 + 100
x = int(x)
print(x)
a = x // 100
b = (x // 10) % 10
c = x % 10
print(a + b + c)