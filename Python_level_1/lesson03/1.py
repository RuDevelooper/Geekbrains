# print('hello')
# len('qweqweqwe')
#
# for i in range(1, 10, 2):
#     print(i)
#
# abs(-10)
# print(max([4, 5, 6, 7]))
# print(max(['zzz', 'xxx', 'ccc'], key=len))
# print(sum([4, 5, 6, 7]))
# print(type(4))
# print(type('wertwe'))
# print(type([1, 2]))
#
# name = input('ФИО')
#
# def name_check(name_to_check):
#     if len(name_to_check.split()) == 3:
#         print(name_to_check.title())
#     else:
#         print('Некорректно! Попробуйте снова!')
#
# def hello():
#     print('Hello! :)')

# name_check(name)
# hello()

# admin_login = 'Denis'
# admin_pass = 'root'
# def is_admin(login, password):
#     if login == admin_login and password == admin_pass:
#         return True
#     return False
#
# if is_admin('Den', 'qwerty'):
#     print('Привет АДМИН')
# else:
#     print('Привет Гость!')
#
# result = is_admin('Den', 'qwerty')
# print(result)
# result = is_admin('Denis', 'root')
# print(result)

# max(['zzz', 'xxx', 'ccc'], key=len)

# x = 10
#
# def test():
#     global x
#     x = 11
#     print(x)
#     return x
#
# print(x)
# x = test()
# print(x)

# def check_name(name, surname='', middle_name='', age=''):
#     print(name, surname)
#
# check_name('Ivan')
# check_name(surname='Petrov', name='Ivan')

# def check_name(*args):
#     for arg in args:
#         print (arg, end=' ')
#
# name = ['Иван', 'Петров']
# check_name('Ivan', 'Petrov')


# def check_name(name, *args):
#     print(name)
#     for arg in args:
#         print (arg, end=' ')
#
# check_name('Ivan', 'Petrov')

# def check_name(name='', surname=''):
#     print(name, surname)
#
#
# human = {'name': 'Ivan', 'surname': 'Petrov'}
# check_name(**human)  # name='Ivan', surname='Petrov'

# def check_name(**kwargs):
#     print(name, surname)
#
# human={'name': 'Ivan', 'surname': 'Petrov'}
# check_name(**human) # name='Ivan', surname='Petrov'

# f = lambda x: x + 2
# print(f(2))

# values = [-1, 2, 3, 4, 5]
# print(list(map(lambda x : x ** 2, values)))
#
# zip()
#
# print(list(filter(lambda x : x > 2, values)))
# # filter возвращает только если условие истина
#
# f = open('100.txt', 'r', encoding='UTF-8')
# print(f.readlines())
# f.close()
#
# with open('100.txt') as f:
#     for line in f:
#         print(f)

# print('hello')
# len('qweqweqwe')
# input('asdasd')

# for i in range(10):
#     print(i)

# abs(-10)
# print(max([4, 5, 6, 7]))
# print(max(['zzz', 'aaaa', 'cc'], key=len))
# print(sum([4, 5, 6, 7]))
# print(type(4))
# print(type('asda'))
# print(type([1,2]))


# name = input('Р¤РРћ:')
#
#
# def name_check(name_to_check):
#     if len(name_to_check.split()) == 3:
#         print(name_to_check.title())
#     else:
#         print('РќРµРєРѕСЂСЂРµРєС‚РЅРѕ! РџРѕРїСЂРѕР±СѓР№С‚Рµ СЃРЅРѕРІР°!')

# admin_login = 'root'
# admin_pass = '*dv238df283dv92'
#
# def is_admin(login, password):
#     if login == admin_login and password == admin_pass:
#         return True
#     return False
#
# if is_admin('Vasya', 'qwerty'):
#     print('РџСЂРёРІРµС‚ Р°РґРјРёРЅ!')
# else:
#     print('РџСЂРёРІРµС‚ РіРѕСЃС‚СЊ!')
#
# result = is_admin('root', '*dv238df283dv92')
# print(result)

# max(['asdasd', 'asdasd'], key=len)

# x = 10

# def test():
#     global x
#     x = 11
#     print(x)

# def test():
#     x = 11
#     return x
#
# print(x)
# x = test()
# print(x)


# def check_name(name, surname='', middle_name='', age='',):
#     print(name, surname, middle_name, age)
#
# check_name('Ivan', 'Petrov')
# check_name('Ivan', age=20)

# def check_name(*args):
#     print(args)
#     print(type(list(args)))
#     for arg in args:
#         print(arg, end=' ')
#
# name = ['РРІР°РЅ', 'РџРµС‚СЂРѕРІ', 'РђРЅР°С‚РѕР»СЊРµРІРёС‡']
# check_name(*name) # РєР°Р¶РґС‹Р№ СЌР»РµРјРµРЅС‚ СЃРїРёСЃРєР°, РєР°Рє СЃР°РјРѕСЃС‚РѕСЏС‚РµР»СЊРЅС‹Р№ Р°СЂРіСѓРјРµРЅС‚

# def check_name(name, surname='', *args):
#     print(name, surname)
#     for arg in args:
#         print(arg, end=' ')
#
# check_name('Ivan', 'Petrov', 'Vasiljevich')

# x = (1, 2, 34)
# y = list(x)
# print(x, y)

# def check_name(name='', surname=''):
#     print(name, surname)
#
# human = {'name': 'Ivan', 'surname': 'Petrov'}
# check_name(**human) # name='Ivan', surname='Petrov'

# def check_name(x, y='', *args, **kwargs):
#     print(x, y, args, kwargs)
#
# human = {'name': 'Ivan', 'surname': 'Petrov'}
# check_name(10, 20, 1,2,3,4,5,6,7, name='Ivan', surname='Petrov')  # name='Ivan', surname='Petrov'

# f = lambda x: x ** 2
# print(f(2))

# names = ['Ivan', 'Oleg', 'Alena']
# salary = [100, 200]
# print(dict(zip(names, salary)))
# print(list(zip(names, salary)))
# print(tuple(zip(names, salary)))

# def test(x):
#     return x ** 2
#
#
# values = [-1, -2, 3, 4, 5]

# print(list(map(lambda x: x ** 2, values)))
# print(list(map(test, values)))
# print(map(test, values))
# print(list(filter(lambda x: x > 0, values)))

# f = open('100.txt', 'r', encoding='UTF-8')
# print(f.readlines())
# for line in f:
#     print(line.strip())
# f.close()

# f = open('123.txt', 'a', encoding='UTF-8')
# f.write('asd\n')

# f.close()

# with open('100.txt') as f:
#     for line in f:
#         print(line)

def strlong(*args):
    x = 0
    for arg in args:
        if len(arg) > x:
            x = len(arg)
            maxlen = arg
        else:
            pass
    print(maxlen)
    return maxlen

name = ['Иван', 'Петров', 'Анатольевич']
strlong(*name)
print(strlong(*name))