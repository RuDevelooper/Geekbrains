#!/usr/bin/env python3

# Создание замыкания

def func(x, y):

    return x + y

def closure(x):

    return func(x, 10)

#############################################################################

# Фабрика замыканий

def factory(y):

    def func(x):

        return x + y

    return func

f = factory(37)
g = factory(40)

print(f(1), f(2), f(3))
print(g(1), g(2), g(3))

