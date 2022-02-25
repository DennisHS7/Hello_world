#1
s1 = input("Inter your name:")
s2 = "Hello " + s1
s3 = s1*3
print(s2)
print(s3)
#2
import random
x = random.randint(100, 900)
print(x)
s = str(x)
a = int(s[0])
b = int(s[1])
c = int(s[2])
print(a + b + c)
#3
s = input("Enter something ")
print(s[::3])
print(s[:1] + s[-1:])
print(s.upper())
print(s[::-1])
print(s.isdigit())
#4
s = input("Enter something ")
if s.lower() == s[::-1].lower():
    print("This is a palindrome")
else:
    print("This is not a palindrom")
#Home work
s = input("Enter something ")
print(s[2])
print(s[-2])
print(s[0:5])
print(s[:-2])
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s[::-2])
print(len(s))