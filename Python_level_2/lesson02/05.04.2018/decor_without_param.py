#!/usr/bin/env python3

def sample(f):

    def wrap(*args, **kwargs):

        print("Before", *args)

        lst = list(args)
        res = f(lst)

        print("After")

        return res

    return wrap

@sample
def func(lst):

    return sum(lst)

print(func(3, 7))
print(func(2, 5, 6, 3, 4))

