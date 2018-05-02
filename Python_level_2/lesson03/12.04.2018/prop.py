#!/usr/bin/env python3

class CProp:

    def __init__(self):

        self.__x = 10

    @property
    def x(self):

        print("IN")
        return self.__x

    @x.setter
    def x(self, value):

        print("SET")
        self.__x = value

obj = CProp()

obj.x = 111

print(obj.x)

