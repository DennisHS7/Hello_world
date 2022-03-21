1

def credit_card(card):
    return '*' * len(card[:-4]) + card[-4:]


print(credit_card(input("Enter credit card number: ")))

2

def palindrome(data):
    data = data.replace(' ', '').lower()
    return 'palindrome' if data == data[::-1] else 'not a palindrome'


print(palindrome(input("Enter a word: ")))

3

class Tomato:
    states = {0: 'non', 1: 'green', 2: 'yellow', 3: 'red'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        self._change_state()

    def is_ripe(self):
        if self._state == 3:
            return True
        return False

    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()

    def _print_state(self):
        print(f'Tomato {self._index} is {Tomato.states[self._state]}')


class TomatoBush:
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print('Gardener is working... ')
        self._plant.grow_all()
        print('Gardener finished')

    def harvest(self):
        print('Start harvesting...')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Harvesting is end.')
        else:
            print('Your tomatoes are not ripe.')

    @staticmethod
    def knowledge_base():
        print('''Three stages of maturation: green, yellow, red.''')


if __name__ == '__main__':
    Gardener.knowledge_base()
    great_tomato_bush = TomatoBush(4)
    gardener = Gardener('Dennis', great_tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()
