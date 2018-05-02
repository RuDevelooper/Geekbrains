#!/usr/bin/env python3

class CCls:

    __slots__ = ('x', 'y', 'z')

    def __init__(self):

        self.x = 10
        self.y = 20

    def fn(self):

        self.z = 30

    def fn_2(self):

        print(self.z)

obj_1 = CCls()
obj_2 = CCls()

obj_1.x = 50
obj_2.x = 70

print(obj_1.x, obj_2.x)

CCls.x = 777

print(obj_1.x, obj_2.x)

