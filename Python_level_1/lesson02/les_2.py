# print('Hello' + 'world!')
# print('Hello', 'world!')
# print('Hello ' * 3)
#
# email = 'user@mail.com'
# print(email[4])
#
# print(email[5:9])
#
# print(email[::-1])
#
# print('иван петрОв'.title())
# print('иван петрОв'.upper())
# print('иван петрОв'.lower())
# print('иван петрОв'.find('пет', 6))

# name = 'Иван'
# surname = 'Петров'
# age = 20
# print('Привет, %s %s которому %i лет' % (name, surname, age))
# print('Привет, {} {} которому {} лет'.format(name, surname, age))
# print('Привет, {2} {1} которому {0} лет'.format(name, surname, age))

# peoples = ['Alice', 'Bob', 'Alex']
# print(peoples[0])
# print(peoples[1:])
# print(peoples[-1])
# print(peoples + ['Sergey', 'Yana'])

# peoples[0] = 'Maxim'
# print(peoples)
# peoples.append('Egor')
# print(*peoples)
# peoples.pop()
#
# print('Alice' in ['Bob', 'Alex', 'Alice'])

# some_typle = (2, 3, 4, 5)
# print(some_typle + (6, 7, 8))

# i = 0
# while i < len(peoples):
#     print(peoples[i])
#     i += 1

# for item in peoples:
#     print(item)
#
#
# print(item)

# bank_accounts = {'Alice': 100.20, 'Bob': 200.10}
# print(bank_accounts['Alice'])
# print(bank_accounts['Bob'])
# print(bank_accounts)
#
# bank_accounts['Alice'] = 500.10
# print(bank_accounts['Alice'])
# bank_accounts['Alex'] = 20
# print(bank_accounts)


# bank_accounts = {'Alice': 100.20, 'Bob': 200.10}
# for name in bank_accounts.keys():
#     print(name)
#
# for money in bank_accounts.values():
#     print(money)
#
# for name, money in bank_accounts.items():
#     print(name, money)

my_list = [1, 2, 3, 4, 5, 6, 6, 6, 7]
my_list2 = [6, 7, 8, 8, 9, 1, 5]
print(my_list)
my_set = set(my_list) #множество
my_set2 = set(my_list2)
print(my_set)
print(my_set & my_set2)
print(my_set - my_set2)
print(my_set | my_set2)

