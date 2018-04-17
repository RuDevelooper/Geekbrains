# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('В движении.')

    def stop(self):
        print('Остановились.')

    def turn(self, direction):
        if direction == 'left':
            print('Повернули на лево.')
        elif direction == 'right':
            print('Повернули на право.')


class TownCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)


class SportCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)


class WorkCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)


car = PoliceCar(100, 'black', 'Porche')

print('При создании экземпляра классе переданы:', *car.__dict__.values())

car.go()
car.turn('right')
car.stop()
