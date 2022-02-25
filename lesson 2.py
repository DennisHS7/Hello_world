# Определить, является ли год високосным.
year = int(input("Введите год "))
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('Високосный')
else:
    print('Не високосный')

# Определить существование треугольника и его тип
print("Введите стороны треугольника:")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a + b <= c or b + c <= a or c + a <= b:
    print("треугольник не существует")
elif a != b and b != c and c != a:
    print("Разносторонний")
elif a == b == c:
    print("Равносторонний")
else:
    print("Равнобедренный")

# Определить принодлежность точки кругу
import math

print("Введите координаты точки и радиус круга:")
x = int(input("x = "))
y = int(input("y = "))
r = int(input("r = "))

hypotenyse = math.sqrt(x ** 2 + y ** 2)

if hypotenyse <= r:
    print("точка принадлежит кругу")
else:
    print("точка не принадлежит кругу")


