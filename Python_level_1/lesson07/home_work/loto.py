#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11      
      16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import random


class Chips:

    def __init__(self):
        self._sack_with_chips = [i for i in range(1, 91)]


    def get_new(self):

        try:
            chip = self._sack_with_chips.pop(random.randint(1, len(self._sack_with_chips)) - 1)
            print('Бочонок:', chip, 'Осталось: %s' % len(self._sack_with_chips))
        except ValueError:
            return print('Пусто')
        return chip


class Cards:

    def __init__(self):
        self.card = self._generate_card()
        self.i = 0

    def _generate_card(self):
        new_card = [[None for _ in range(9)] for _ in range(3)]
        i = 0
        while i < 15:
            value = random.randint(1, 90)
            column = value // 10 if value != 90 else 8
            # print(*zip(new_card))
            for _ in new_card:
                line = random.randint(0, 2)
                if new_card[line][column] is None and not (value in list(zip(*new_card))[column]):
                    new_card[line][column] = value
                    i += 1
                    break
        return new_card

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.card):
            self.i += 1
            return self.card[self.i - 1]
        else:
            self.i = 0
            raise StopIteration


    def prnt(self):
        print('-' * 54)
        for line in self.card:
            for elem in line:
                print(str(elem).rjust(5, ' ') if not elem is None else ' ' * 5, end='|')
            print()
            print('-' * 54)


            # print(line[value // 10] if value != 90 else line[8])

    def is_in(self, chip):
        for line in self:
            if chip in line:
                return True

    def cross_out(self, num):
        for index, line in enumerate(self.card):
            for num_index, value in enumerate(line):
                if value == num:
                    print(self.card[index][num_index])
                    self.card[index][num_index] = '-'



class Loto:

    def __init__(self, name_1, name_2):
        self.player_1 = name_1
        self.player_2 = name_2

    def _game(self):
        self._play_1 = Cards()
        self._play_2 = Cards()
        chip = Chips()
        self._play_1._hit = 0
        self._play_2._hit = 0
        while self._play_1._hit < 15 and self._play_2._hit < 15:
            try:
                i = chip.get_new()
            except TypeError:
                print('Ничья! НЕНУАЧО?!\nБочонки закончились а циферки еще есть. ЧЯДНТ??? ')
                break
            print('{:^54}'.format(self.player_1))
            self._play_1.prnt()
            print('{:^54}'.format(self.player_2))
            self._play_2.prnt()
            if self._play_2.is_in(i):
                self._play_2.cross_out(i)
                self._play_2._hit += 1
            # if self._play_1.is_in(i):
            #     self._play_1.cross_out(i)
            #     self._play_1._hit += 1

            if self._play_1.is_in(i):
                if input('На вашей карточке есть цифра %s. Зачеркнуть? (y/n)' %i).upper() == 'Y':
                    self._play_1.cross_out(i)
                    self._play_1._hit += 1
                else:
                    print(self.player_1, 'проиграл :(')
                    break
        if self._play_1._hit == 15:
            print(self.player_1, 'победил!')
        else:
            print(self.player_1, 'проиграл :(')


a = Loto('Игрок', 'Компьютер')

a._game()

