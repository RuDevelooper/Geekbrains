# Замыкания (closures)

# Создание замыкания
#
# def func(x, y):
#
#     return x + y
#
# def closure(x):
#
#     return func(x, 10)


# Фабрика замыканий

def factory(y):
    def func(x):
        return x + y

    return func


f = factory(37)
g = factory(40)

print(f(1), f(2), f(3))
print(g(1), g(2), g(3))


def meta_sample(c):
    def sample(f):
        def wrap(*args, **kwargs):
            print('Before')
            lst = list(args)
            lst.append(c)

            res = f(lst)

            print('After')

            return res

        return wrap

    return sample


@meta_sample(5)
def func(lst):
    return sum(lst)


# sample(func(10, 20))

print(func(5, 6, 10, 20))

# Менеджеры контекста

# with open('file.txt') as fl:
#     fl.read(1024)

############

# class CWith():
#
#     def __enter__(self):
#
#         # self.db
#
#         self.db.stert_transaction()
#
#         return self.db.cursor()
#
#     def __exit__(self, err, value, tb):
#
#         self.db.commit()
#
# conn = CWith()
#
# with conn as cursor:
#

#     cursor.update(...)


# Модуль select()

import select

sock = [ ... ] # Дочерние сокеты

ready_for_read, ready_for_write, sock_with_error = \
    select.select(sock, sock, sock, timeout = 1)

for s in ready_for_read:

    s.recv(1024)

import logging
import logging.handlers

logger = logging.getLogger('test_log')

formatter = \
    logging.Formatter('%(asctime)s - %(levelname)s - %(message)s ')

fn = logging.FileHandler('log.log')
fn.setLevel(logging.DEBUG)
fn.setFormatter(formatter)

logger.addHandler(fn)
logger.setLevel(logging.DEBUG)


logger.info('TODO')