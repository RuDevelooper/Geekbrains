#!/usr/bin/python

class CBase:

    def fn(self):

        print("IN Base")

class CChild(CBase):

    pass

    """
    def fn(self):

        super().fn()
        CBase.fn(self)

        print("IN child")
    """

obj = CChild()
obj.fn()

