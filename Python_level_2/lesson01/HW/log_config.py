#!/usr/bin/env python3

import sys
import logging
from logging.handlers import TimedRotatingFileHandler

# Определить формат сообщений
msg_format = logging.Formatter('<%(asctime)s> <%(levelname)s> '
                               '<%(module)s> <%(funcName)s><%(message)s>')

# Создать обработчик, который выводит сообщения в файл
# (перезаписываем каждый день в 00:00)

hand = TimedRotatingFileHandler(filename='log.log', when='midnight', encoding='utf8')
hand.setLevel(logging.INFO)
hand.setFormatter(msg_format)

# Создать регистратор верхнего уровня с именем ‘app’

logger = logging.getLogger('app')
logger.setLevel(logging.INFO)

logger.addHandler(hand)
hand.setLevel(logging.INFO)


# Создать декоратор @log для фиксирования обращения к функции и переданных в нее аргументов

def log(func):
    name = func.__name__
    call = func.__call__
    print(dir(func))
    logger.info(name)
    logger.info(call)
    caller = sys._getframe(1).f_code.co_name

    def wrap(*args, **kwargs):
        logger.info('Обращение к %s от %s с аргументами %s' % (name, caller, args))
        return func(*args)

    return wrap


#
#
# def foo():
#     print "I am foo, calling bar:"
#     bar()
#
# def bar():
#     print "I am bar, calling baz:"
#     baz()
#
# def baz():
#     print "I am baz:"
#     caller = sys._getframe(1).f_code.co_name
#     callers_caller = sys._getframe(2).f_code.co_name
#     print "I was called from", caller
#     print caller, "was called from", callers_caller
#
# foo()