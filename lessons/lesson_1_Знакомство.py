# char symbol = 'g' - c language
# it is variable name
name = "Petr"
# it is variable surname
surname = "Petrov"

age = 100

married = True

mark = 7.9

print("name: ", name, type(name), "\n",
      "surname: ", surname, type(surname), "\n",
      "age: ", age, type(age), "\n",
      "married: ", married, type(married), "\n",
      "mark: ", mark, type(mark))

a = 10 * (12 + 13)

print("%", a % 200)
print("/", a / 200)
print("//", a // 200)

number1 = 10
number2 = 20

result = number1 - number2

print("a - b = ", result)

result = number1 + number2
print("a + b = ", result)

result = number1 * number2
print("a * b = ", result)

result = number1 / number2
print("a / b = ", result)

result = number1 // number2
print("a // b = ", result)

result = number1 % number2
print("a % b = ", result)

result = number1 ** (number2 - number1)
print("a ** b = ", result)

# default
nickname = ''
age = 0

# False it is cash
card_or_cash = False

print("Welcome to Yandex taxi application!!")
# nickname = input("Please enter your nickname: ")
# age = int(input("Please enter your age: "))
# pay = int(input("Choose pay 1 - cash, 2 - card: "))

# print("Welcome,", nickname, "you are ", age, "years old", "you pay", "cash" if pay == 1 else "card")
# print(type(age))

number_float = int(float(input("enter anything float: ")))
print(number_float, type(number_float))

value_bool = bool(input("enter bool value: "))
print(value_bool, type(value_bool))

print(bool(0), bool(-100))