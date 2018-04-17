# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный класс, который наследуется от базового - Игрушка

class Toy:
    def __init__(self, name, color, type_of_toy):
        self.name = name
        self.color = color
        self.type_of_toy = type_of_toy


class AnimalToy(Toy):

    def __init__(self, name, color, type_of_toy):
        super().__init__(name, color, type_of_toy)


class CartoonCharacter(Toy):

    def __init__(self, name, color, type_of_toy):
        super().__init__(name, color, type_of_toy)


class Factory:

    def purchase_of_raw_materials(self):
        print('Закупка сырья\n')

    def sewing_toy(self):
        print('Пошив игрушки\n')

    def painting_toy(self):
        print('Покраска игрушки\n')

    def make_toy(self, name, color, type_of_toy):
        if type_of_toy == 'Животное':
            return AnimalToy(name, color, type_of_toy)
        elif type_of_toy == 'Персонаж мультфильма':
            return CartoonCharacter(name, color, type_of_toy)


# type('Toy', (), {'name': self.name, 'color': self.color, 'type_of_toy': self.type_of_toy})



a = Factory().make_toy('Маша', 'Красный', 'Персонаж мультфильма')

b = Factory().make_toy('Мишка', 'Бурый', 'Животное')

Factory().purchase_of_raw_materials()

Factory().sewing_toy()

Factory().painting_toy()

print('Переданы атрибуты: {}, {}, {}\nПолучен объект класса: {}\n'
      .format(*a.__dict__.values(), type(a).__name__))

print('Переданы атрибуты: {}, {}, {}\nПолучен объект класса: {}\n'
      .format(*b.__dict__.values(), type(b).__name__))