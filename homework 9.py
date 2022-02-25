# 1 Провперить, есть ли в последовательности дубликаты.

# lst = [0, 1, 1, 2, 3, 3, 4, 5, 5, 6]
#
# st = set(lst)
#
# print(len(st) == len(lst))

# 2

# Изменяемое множествою

# st = {'it', 'is', 'set', 1}

# Неизменяемое множество.

# frozen_st = frozenset({'it', 'is', 'frozen', 'set', 2})

# Объединение множеств.

# union = st | frozen_st

# операция пересечения созданных множеств

# intersection = st & frozen_st

# 3 создаём словарь

dct = {1: 'text1', 2: 'text2', 3: 'text3'}

# Добавить новый элемент с ключом типа str и значением типа int

dct['str_key'] = 12345
print(dct)

#  Добавить новый элемент с ключом типа кортеж(tuple) и значением типа список(list)

dct[('it', 'is', 'tuple')] = [11, 22, 'list_value', 33, {1, 2, 3}]
print(dct)

# Получаем элемент словаря по ключу str_key
# Способ 1: Напрямую - в случае отсутствия ключа формируется исключение

item_by_key_v1 = dct['str_key']
print(item_by_key_v1)

# Способ 2: Через функцию get() - в случае отсутствия ключа возвращается
# дефолтное значение 'No item'.

item_by_key_v2 = dct.get('str_key', 'No item')
print(item_by_key_v2)

# Удоляем элемент ключом 2 из словаря

item_deleted = dct.pop(2, 'No item')
print(item_deleted)

# Получаем ключи словаря

keys = dct.keys()
print(keys)