# a = 4
# b = 5
# c = 'asd'
# d = 4.4
# e = True
# f = (1, 2, 3)
#
# def test(some_data):
#     some_data = 100
#
#
# test(a)
# print(a)
#
# a = [1, 2, 3, 4]
#
# def test(some_list):
#     some_list = [1, 2]
#
# def test(some_list):
#     some_list[0] = 100
#
# test(a)
# print(a)

# a = [1, 2, 3, 4]
# for i in a:
#     print(i)
#     a.remove(i)
#
# a = [1, 2, 3, 4]
# for i in a.copy():
#     print(i)
#     a.remove(i)
#
# a = [1, 2, 3, 4]
# for i in a[:]:
#     print(i)
#     a.remove(i)
# import copy
#
#
# some_list = [1, 2, 3, 4, [5, 6, 7]]
# new_list = some_list.copy() # срез работает ттакже
# new_list = some_list.deepcopy(some_list)

# a = [
#     [1, 2, 3],
#     [5, 6, 7],
#     [8, 9, 0]
# ]
#
# a[1][1]

# name = input('Name:')
# print(name or 'Гость')
#
#
# name = input('Name:')
# print(name if name else 'Гость')
#
# age = int(input('Age:'))
#
# print('Доступ разрешен' if age >= 18 else 'В доступе отказано')

# a = 10
# b = 10
# print(a is b)
#
# a = 11
# print(a is b)
#
# some_list = [1, 2]
# nem_list = some_list.copy()
# print(some_list is nem_list)

# some_list = []
#
# for i in range(10):
#     some_list.append(i)
#
# print(some_list)
#
# some_list = [i**2 for i in range(10)]
#
# print(some_list)

# some_list = [i for i in range(-10, 10) if i > 0]
#
# print(some_list)

# names = ['Alex', 'Alice', 'Bob']
# salary = [100, 200, 300]
# my_dict = {key: value for key, value in  zip(names, salary)}
# print(my_dict)

# import re
#
# email = 'test123@mail.ru'
# regex = '[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]+'
# print(re.match(regex, email)) # Ищет строго с начала строки
# print(re.search(regex, email))
# print(re.findall(regex, email))
#
# if email in re.findall(regex, email):
#     print('Ваш email в списке валидных!')
# else:
#     print('Ваш email не корректный!')

try:
    100 / 0
    somr_list
except ZeroDivisionError:
    print()