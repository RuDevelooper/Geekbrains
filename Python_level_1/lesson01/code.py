# PyCharm
# Python.org
# PEP-8
# ctrl + / - РєРѕРјРјРµРЅС‚РёСЂРѕРІР°РЅРёРµ
# pastebin.com
# РќР• Р”Р•Р›РђР•Рњ Р”Р— Р’ РљРћРќР¦Р• РњР•РўРћР”РР§РљР
# РќР• Р”Р•Р›РђР•Рњ Р”Р— РџРћ РљРќРћРџРљР• Р”РћРњРђРЁРќР•Р• Р—РђР”РђРќРР• РќРђ РЎРђР™РўР•!

# age = 20
# print(age + 2)
# print(age // 3)
# print(age % 3)
# print(age ** 3)

# money = 20.1
# print(money - 1)

# name = 'Sergey'
# print(name)

# is_admin = True
# is_god = False
#
# accounts = ['Sergey', 'Alisa', 'Bob', 200, is_admin]
# accounts_fixed = ('Sergey', 'Alisa', 'Bob', 200, is_admin)
# bank_accounts = {'Alisa': 200.0, 'Bob': 33.23}

# x = 10
# x = 'test'
# print(int('100'))
# print(str(200))
# float(200)
# bool(1)

# name = input('Пожалуста введите ваше имя:')
# print('Привет‚', name)
# #
# age = int(input('Введите возраст:'))
# print(age + 100)

# x = 10
# y = 20
# print(x < y)
# print(x == y)
# print(x <= y)
# print(x > y)
# print(x >= y)
# print(x != y)

# x = 100
#
# if x > 0:
#     print('x больше 0')
# elif x > -50:
#     print('x меньше нуля, но больше -50')
# else:
#     print('x меньше 0')

# secret = 'qwerty'
# password = input('Введите пароль:')
#
# if password == secret:
#     print('Access granted')
#     name = input('Введите имя:')
#     if name == 'admin':
#         print('Привет, админ!')
#     else:
#         print('Привет гость!')
# else:
#     print('Access denied')

# x = 10
#
# if 0 < x < 100:
#     print('....')
#
# if x > 0 and x < 100:
#     print('...')
#
# if x > 0 or x > 100:
#     print('...')
#
# if x < 10:
#     print('...')

# a = 5
# while a > 0:
#     print(a)
#     # a = a - 1
#     a -= 1

incorrect_password_count = 0
secret = 'qwerty'

while incorrect_password_count < 3:
    password = input('Password:')
    if password == secret:
        print('Access granted')
        break # РѕСЃС‚Р°РЅР°РІР»РёРІР°РµС‚ С†РёРєР»
    else:
        incorrect_password_count += 1
else: # РѕС‚СЂР°Р±РѕС‚Р°РµС‚ РµСЃР»Рё С†РёРєР» Р±С‹Р» Р·Р°РІРµСЂС€РµРЅ РєРѕСЂСЂРµРєС‚РЅРѕ
    print('Р’С‹ РёСЃС‡РµСЂРїР°Р»Рё РїРѕРїС‹С‚РєРё РІРІРѕРґР° РїР°СЂРѕР»СЏ!')

a = 10

while a > 0:
    if a % 2 == 0:
        a -= 1
        continue
    print(a)
    a -= 1
