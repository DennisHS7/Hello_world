# 1 Выведите значение возраста из словаря person.

# person = {"name": "Dennis", "age": "33", "city": "Glubokoe"}
# print(person["age"])

# 2 Значениями словаря могут быть и списки.
# Создайте словарь с ключами BMW, Tesla и списками из 3х моделей в качестве значений.
# Выведите первое и последнее значения каждого из ключей.

# models_data = {"BMW": ["Model_1", "Model_2", "Model_3"],
#                "Tesla": ["Model S", "Model A", "Model B"]}
# print(models_data["Tesla"][0], models_data["Tesla"[2]])
# print(models_data["BMW"][0], models_data["BMW"[2]])

# 3 Исправьте ошибки в коде, чтобы получить требуемый вывод. (Вывод True)
# d1 = {"a": 100. "b": 200. "c":300}
# d2 = {a: 300. b: 200, d:400}
#
# print(d1["b"] == d2["b"])

# d1 = {"a": 100, "b": 200, "c": 300}
# d2 = {"a": 300, "b": 200, "c": 400}
# print(d1["b"] == d2["b"])

# 4 Дан словарь с числовыми значениями. Необходимо их все перемножить и вывести на экран.

# my_dictionary = {'data1': 123, 'data2': 467, 'data3': 987, 'data4': 234}
# result = 1
# for key in my_dictionary:
#     result = result * my_dictionary[key]
# print(result)

# 5 Даны два списка одинаковой длины. Необходимо создать из них
# словарь таким образом, чтобы элементы первого списка были ключами,
# а элементы второго — соответственно значениями нашего словаря.

# keys = ['Audi', 'Volvo', 'Maserati']
# values = ['A8', 'XC60', 'Quattroporte']
# cars_dict = dict(zip(keys, values))
# print(cars_dict)

# 6 Создайте словарь из строки 'pythonist' следующим образом:
# в качестве ключей возьмите буквы строки, а значениями пусть будут числа,
# соответствующие количеству вхождений данной буквы в строку.

# str1 = 'pythonist'
# my_dict = {i: str1.count(i) for i in str1}
# print(my_dict)

# Homework У вас есть словарь, где ключ – название продукта. Значение – список,
# который содержит цену и кол-во товара.
# Выведите через ‘’–’’ название – цену – количество.
# С клавиатуры вводите название товара и его кол-во. n – выход из программы.
# Посчитать цену выбранных товаров и сколько товаров осталось в изначальном списке.

while True:
    products = {'fish': ['3', '20'], 'meat': ['5', '30'], 'vegetables': ['2', '25']}
    i = 0
    for pr in products:
        print(pr, '-', products[pr][0], '-', products[pr][1])
        i += 1
    name_prod = input("Enter product name: ")
    numb_prod = input("Enter product numb: ")
