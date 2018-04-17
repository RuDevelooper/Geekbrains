# тестирование класса
# class CCls:
#
#     def fn(self, a, b):
#         pass
#
# a
# b
# m1()
# m2()
#
# Mock
#
# CCls.fn()

# в ДЗ нужно создать config.py и обявлять пространство имен через класс,
# а не через словарь

# перегрузка - переопределение метода в дочернем классе.
# все методы в питоне виртуальные


class CBase:
    def fn(self):
        print('IN base')


class CChild(CBase):

    def fn(self):
        # super().fn() - неявное указание класса для вызова метода

        CBase.fn(self)  # явное указание базового класса для вызова метода
        print('IN child')

    pass


obj = CChild()
obj.fn()


# C3-линеаризация - алгоритм учитывающий порядок наследования в базовых классах,
# выстраивает единый порядок для вызова конкретного метода

# __mro__ - метод класса для просмотра порядка наследования
# __slots__ - позволяет явно перечислить слоты (поля) в конкретном классе

class CCls:
    __slots__ = ('x', 'y')

    def __init__(self):
        self.x = 10
        self.y = 20
        # self.z = 30

        # print(self.__dict__)


obj_1 = CCls()
obj_2 = CCls()
obj_3 = CCls()

obj_2.x = 70
# __dict__ - метод возвращает словарь из полей класса или объекта

print('CCls.__dict__, obj.__dict__', obj_2.x, obj_1.y)

# доступ к полям класса через дескриптор данных

CCls.x = 777
print('CCls.__dict__, obj.__dict__', obj_2.x, obj_1.x)


# ПРОИЗВОДНЫЙ КЛАСС ДОЛЖЕН ОБЪЯВЛЯТЬ __slots__

# дескрипторы класса

# class TypedProperty: # дескриптор доступа к
#
#     pass

class CDesc:

    def __init__(self, name):
        self.__name = name

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]


class CCls_1:
    x = CDesc('x')

    def __init__(self, x):
        self.x = x

    def fn(self):
        print(self.x)


obj_11 = CCls_1(10)
obj_22 = CCls_1(30)

obj_11.fn()
obj_22.fn()


class CProp:

    def __init__(self):
        self.__x = 10

    @property
    def x(self):
        print('IN')
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value
        print('SET')


object = CProp()

object.x

object.x = 30

# модуль socketserver

import socketserver


class CTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        self.request.recv(1024)

        self.request.send(b'asd')


server = socketserver.TCPServer(('127.0.0.1', '7777'), CTCPHandler)

server.serve_forever()
