# # a = 1 + 5
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


# def encrypt(fn):
#     def wrapped():
#         if 'РЎРµРєСЂРµС‚РЅС‹Рµ' in fn():
#             return '****** secret information ******'
#         return fn()
#     return wrapped
#
#
# @encrypt
# def get_secret_data():
#     return 'РЎ1РµРєСЂРµС‚РЅС‹Рµ РґР°РЅРЅС‹Рµ!'
#
# print(get_secret_data())


# def makeupper(fn):
#     def wrapped(name):
#         return fn(name).upper()
#     return wrapped
#
#
# @makeupper
# def get_lower_name(name):
#     return name.lower()
#
# print(get_lower_name('РРіРѕСЂСЊ'))


# def makebold(fn):
#     def wrapped():
#         return "<b>" + fn() + "</b>"
#     return wrapped
#
#
# def makeitalic(fn):
#     def wrapped():
#         return "<i>" + fn() + "</i>"
#     return wrapped
#
#
# @makebold
# @makeitalic
# def hello():
#     return "hello habr"
#
#
# print(hello())  ## РІС‹РІРµРґРµС‚ <b><i>hello habr</i></b>

import os


class LogReader:

    def __init__(self):
        self.files = []

        for file in os.listdir():
            if os.path.isdir(file):
                continue
            if file.startswith('log'):
                file_descriptor = open(file, encoding='UTF-8')
                self.files.append(file_descriptor)

        self.i = 0

    def __del__(self):
        for file_descriptor in self.files:
            file_descriptor.close()
        print('Р¤Р°Р№Р»С‹ Р·Р°РєСЂС‹С‚С‹')

    def __iter__(self):
        return self

    def __next__(self):
        while self.i < len(self.files):
            for line in self.files[self.i]:
                return line
            self.i += 1
        raise StopIteration # Р’С‹Р±СЂР°СЃС‹РІР°РµРј РёСЃРєР»СЋС‡РµРЅРёРµ


log_reader = LogReader()

for i in log_reader:
    print(i.strip())


print('С‚РµСЃС‚')