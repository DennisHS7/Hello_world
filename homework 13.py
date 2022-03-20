# class TheExample:
#     def __init__(self):
#         self.func4()
#
#     def func(self):
#         return self.a + self.b
#
#     def func1(self):
#         return self.a - self.b
#
#     def func2(self):
#         return self.a * self.b
#
#     def func3(self):
#         if self.b == 0:
#             return "error"
#         else:
#             return self.a / self.b
#
#     def func4(self):
#         self.a = int(input())
#         self.b = int(input())
#
#
# while True:
#     print("+,-,*,/")
#     x = input()
#     print("Numbers: ")
#     example = TheExample()
#     if x == "6":
#         break
#     if x == "+":
#         print(example.func())
#     if x == "-":
#         print(example.func1())
#     if x == "*":
#         print(example.func2())
#     if x == "/":
#         print(example.func3())

# class Human:
#
#     # static fields
#     # Статические поля
#     default_name = 'No name'
#     default_age = 0
#
#     def __init__(self, name=default_name, age=default_age):
#         # Динамические поля, Публичные
#         # Dynamic fields, public
#         self.name = name
#         self.age = age
#         # Private, приватные
#         self.__money = 0
#         self.house = None
#
#     def info(self):
#         print(f'Name: {self.name}')
#         print(f'Age: {self.age}')
#         print(f'Money: {self.__money}')
#         print(f'House: {self.house}')
#
#     @staticmethod
#     def default_info(self):
#         print(f'Default Name: {Human.default_name}')
#         print(f'Default Age: {Human.default_age}')
#
#     def earn_money(self, amount):
#         self.__money += amount
#         print(f'Earned {amount} money! Current value: {self.__money}')
#
#
# if __name__ == '__main__':
#
#     Human.default_info(None)
#
#     alexander = Human('Sasha', 27)
#     alexander.info()
#
#     alexander.earn_money(5000)
#     alexander.earn_money(20000)
#     alexander.info()

# HW

# class Tomato:
#     states = {0: 'non', 1: 'flower', 2: 'green', 3: 'red'}
#
#     def __init__(self, index):
#         self._index = index
#         self._state = 0
#
#     def grow(self):
#         self._change_state()
#
#     def is_ripe(self):
#         if self._state == 3:
#             return True
#         return False
#
#     def _change_state(self):
#         if self._state < 3:
#             self._state += 1
#         self._print_state()
#
#     def _print_state(self):
#         print(f'Tomato {self._index} is {Tomato.states[self._state]}')
#
#
# class TomatoBush:
#     def __init__(self, num):
#         self.tomatoes = [Tomato(index) for index in range(0, num)]
#
#     def grow_all(self):
#         for tomato in self.tomatoes:
#             tomato.grow()
#
#     def all_are_ripe(self):
#         return all([tomato.is_ripe() for tomato in self.tomatoes])
#
#     def give_away_all(self):
#         self.tomatoes = []
#
#
# class Gardener:
#     def __init__(self, name, plant):
#         self.name = name
#         self._plant = plant
#
#     def work(self):
#         print('Gardener is working... ')
#         self._plant.grow_all()
#         print('Gardener finished')
#
#     def harvest(self):
#         print('Gardener is harvesting...')
#         if self._plant.all_are_ripe():
#             self._plant.give_away_all()
#             print('Harvesting is finished')
#         else:
#             print('Too early! Your platn is green and not ripe.')
#
#     @staticmethod
#     def knowledge_base():
#         print('''Harvest time for tomatoes should ideally occur
#         when the fruit is a mature green and
#         then allowed to ripen off the vine.
#         This prevents splitting or bruising
#         and allows for a measure of control over the ripening process.''')
#
#     if __name__ == '__main__':
#         Gardener.knowledge_base()
#         great_tomato_bush = TomatoBush(4)
#         gardener = Gardener('Emilio', great_tomato_bush)
#         gardener.work()
#         gardener.work()
#         gardener.harvest()
#         gardener.work()
#         gardener.harvest()

