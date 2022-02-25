num1 = 5
num2 = 10.0

# ==
print("==")
print(num1 == num2)
print(num1 + 5 == num2)
print(True == False)

print("str" == "str")
print("str" == ('s' + 't' + 'r'))
print(len("str") == len("str"))
print("str1" == "str2")

print(5 == 5.0)
print(num1 is num2)

# !=
print("!=")
num3 = 10
num4 = 11.0

print(num3 != num4)
print(5 != 5.0)

print(5 != 10)

# <, >, <=, >=
print("# <, >, <=, >=")

print(num2 > num1)
print(num2 < num1)
print(num3 >= num4)
print(num3 <= num4)

# -------------------------
# ascii table

if False:
    print("true")
    print("true2")
    print("true3")

print("if not works")

if num2 >= num1:
    print("if works")
    num5 = 20
else:
    print("else works")
    num5 = 30

print("num5 = ", num5)

if num3 < 10:
    num5 = 40
elif num3 < 20:
    num5 = 50
elif num3 == 100:
    num5 = 1000
elif num3 < 20:
    num5 = 50
elif num3 == 100:
    num5 = 1000
elif num3 < 20:
    num5 = 50
elif num3 == 100:
    num5 = 1000
else:
    print("nothing")

print(num5)

# and, or, not // &&, ||, !()

num6 = 6
num7 = 10
num8 = 15

# 1 1 -> 1
# 1 0 -> 0
# 0 1 -> 0
# 0 0 -> 0

if (num6 + num7) > num8 and (num8 - num7) < num6:
    print("and works")
else:
    print("and doesn't work")

if (num6 + num7) > num8:
    if (num8 - num7) < num6:
        print("and works")
    else:
        print("and doesn't work")
else:
    print("and doesn't work")

# 1 1 -> 1
# 1 0 -> 1
# 0 1 -> 1
# 0 0 -> 0
# 0 0 0 0 0 0 0 0 0 1 -> 1

if (num6 - num7) > num8 or (num8 + num7) < num6:
    print("if or works")
else:
    print("else or work")

# !0 -> 1
# !1 -> 0

b = False

if not b:
    print("if not")
else:
    print("else not")

num9 = None

if num9:
    num9 = 10
    print(num9)

print("after if")
# --------------------------------------

number = input("number: ")

number = int(number)

number = number + number

if number >= 10:
    number = number // 10
else:
    number = number * 10

print("number= ", number)

# --------------------------------
# 1. enter digit
# 2. ...

student1 = 10
student2 = 7
student3 = 3

if student1 >= 5:
    print("student next class")
else:
    print("student one more first class")

if student2 >= 5:
    print("student next class")
else:
    print("student one more first class")

if student3 >= 5:
    print("student next class")
else:
    print("student one more first class")

print()

if 5 <= student2 <= 10:
    print("next")