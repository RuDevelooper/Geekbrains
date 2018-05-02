#!/usr/bin/env python3

def meta_sample(c):

    def sample(f):

        def wrap(*args, **kwargs):

            print("Before", *args)

            lst = list(args)
            lst.append(c)

            res = f(lst)

            print("After")

            return res

        return wrap

    return sample

@meta_sample(10)
def func(lst):

    return sum(lst)

print(func(3, 7))
print(func(2, 5, 6, 3, 4))

