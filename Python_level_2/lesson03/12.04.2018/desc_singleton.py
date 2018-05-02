#!/usr/bin/env python3

class CDesc:

    def __init__(self, name):

        self.__name = name
        self.__value = None

    def __set__(self, instance, value):

        self.__value = value

    def __get__(self, instance, cls):

        return self.__value

class CCls:

    x = CDesc("x")

    def __init__(self, x):

        self.x = x

    def fn(self):

        print(self.x)

obj_1 = CCls(10)
obj_2 = CCls(30)

obj_1.fn()
obj_2.fn()

