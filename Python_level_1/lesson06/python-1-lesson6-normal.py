# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше
# усмотрение.
import random


class Person:

    def __init__(self, health, damage, armor):
        self.health = int(health)
        self.damage = int(damage)
        self.armor = int(armor)

    def _damage_to(self, opponent):
        return (100 - opponent.armor) / 100 * self.damage

    def attack_to(self, opponent):
        opponent.health = opponent.health - self._damage_to(opponent)
        print(opponent.name, 'атакован!')


class Player(Person):

    def __init__(self, health, damage, armor):
        self.name = 'Игрок'
        super().__init__(health, damage, armor)


class Enemy(Person):

    def __init__(self, health, damage, armor):
        self.name = 'Враг'
        super().__init__(health, damage, armor)


class Fight:

    def __init__(self, opponent_1, opponent_2):
        print('%s\t\t\t%s' % (opponent_1.name, opponent_2.name))
        print('Здоровье:', opponent_1.health, '\tЗдоровье:', opponent_2.health)
        print('Урон:', opponent_1.damage, '\t\tУрон:', opponent_2.damage)
        print('Броня:', opponent_1.armor, '\t\tБроня:', opponent_2.armor)
        print()
        who_attack = random.randint(0, 1)
        print('Первым будет атаковать {}!\n'.format(opponent_1.name if who_attack == 0 else opponent_2.name))
        while True:
            if opponent_1.health <= 0:
                print('{} победил!\n'.format(opponent_2.name))
                break
            elif opponent_2.health <= 0:
                print('{} победил!\n'.format(opponent_1.name))
                break
            if who_attack == 0:
                opponent_1.attack_to(opponent_2)
            else:
                opponent_2.attack_to(opponent_1)
            print('Здоровье:', opponent_1.health, '\tЗдоровье:', opponent_2.health)
            print()

            who_attack = random.randint(0, 1)

# броня указывается в процентах, т.е. 0 - c голым торсом, 100 - surprise, motherfucker!
player = Player(100, 50, 70)
enemy = Enemy(100, 40, 80)

Fight(player, enemy)
