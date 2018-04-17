# coding: utf-8

import sys

class BadNumber(Exception):

    def __init__(self, x):
        self.x = x
    
    def __str__(self):
        return '! ****  Нехорошее число: {} ****'.format(self.x)
        
        

f = open('numbers.txt')

for line in f:
    try:
        x = int(line.strip())
        if x == 13:
            raise BadNumber(x)
    except ValueError:
        print('Ошибка перевода числа в int')
        sys.exit(13)
    except BadNumber as bn:
        print(bn)
        
    else:
        print(x)
        try:
            y = 1000 / x
        except ZeroDivisionError as z:
            print(z)
        else:    
            print(y)
    finally:
        print('Выходим из блока try')
            
            
# a = 1 + 5
#
# class Car:
#
#     def __init__(self):
#         self.modules = []
#
#     def __str__(self):
#         return str(self.modules)
#
#     def add_module(self, module):
#         self.modules.append(module)
#
#     def __add__(self, other):
#         self.modules.append(other)
#         return self
#
# car = Car()
# car = car + 'РєРѕРЅРґРёС†РёРѕРЅРµСЂ'
# car.add_module('Р“РёРґСЂРѕСѓСЃРёР»РёС‚РµР»СЊ СЂСѓР»СЏ')
# print(car)


# class Test:
#
#     @staticmethod
#     def say(what):
#         print(what)
#
# Test.say("asdasdasd")


class my_dict(dict):

    def __setitem__(self, key, value):
        print(key, value)
        return super().__setitem__(key, value)

    def __getitem__(self, item):
        print('РџРѕРїС‹С‚РєР° РїРѕР»СѓС‡РёС‚СЊ Р·РЅР°С‡РµРЅРёРµ РїРѕ РєР»СЋС‡Сѓ', item)
        return super().__getitem__(item)


my_cool_dict = my_dict()
my_cool_dict['test'] = 'qwerty'
print(my_cool_dict)

print(my_cool_dict['test'])