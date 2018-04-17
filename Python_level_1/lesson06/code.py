# ОБъект -

# human = {'name': 'Ivan', 'age': 20}
#
#
# def say(who, what_to_say):
#     print(who['name'], what_to_say)
#
#
# say(human, 'Привет')
#
#
# class Human:  # с заглавной буквы и CamelCase
#
#     def __init__(self, human_name):
#         self._name = human_name
#         self._legs = 2
#
#     def _set_name(self, human):
#         if len(human_name) <= 2
#             return
#         self._name = human_name
#
#     def get_name(self):
#         return self._name
#
#     @property
#     def legs(self):
#         return self._legs
#
#     def say(self, what_to_say):
#         print(self._name, what_to_say)
#
#
# new_human = Human('Иван')
# new_human.say('Hello!')


# Инкапсуляция (сокрытие свойств) в языке Python является не строгой
#
# Паттерны проектирования Ерик Фримен, Элизабет Фримен
# Чистый код - Роберт Мартин


# class BaseDuck:
#
#     def __init__(self, color, duck_type):
#         self.color = color
#         self.type = duck_type
#
#
# class Duck(BaseDuck):
#
#     def fly(self):
#         print('flying!')
#
#
# class WoodenDuck(BaseDuck):
#
#     def be_like_a_duck(self):
#         print('Be like a duck!')
#
#
# class HuntDuck(BaseDuck):
#
#     def __init__(self, color, type, volume):
#         super().__init__(color, type)
#         self.volume = volume
#
#     def make_sound(self):
#         print('Criaaa!')


class Animal:
    def __init__(self, name):
        self.name = name

    def run_from_fire(self):
        print(self.name, 'бежит от пожара')


class Bear(Animal):

    def eat(self):
        print(self.name, 'уст мед')


class Duck(Animal):

    def run_from_fire(self):
        print(self.name, 'летит от пожара')


class Mouse(Animal):

    def run_from_fire(self):
        print(self.name, 'прячется в норе')


def make_fire(*animals):
    for animal in animals:
        animal.run_from_fire()


bear = Bear('Медведь')
duck = Duck('Утка')
mouse = Mouse('Мышка')

make_fire(bear, duck, mouse)
