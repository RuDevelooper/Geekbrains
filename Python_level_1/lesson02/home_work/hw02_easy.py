# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ["яблоко", "банан", "киви", "арбуз"]
for fruit in fruits:
    print('{}. {:>6}'.format(fruits.index(fruit) + 1, fruit))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
print()

random_list_1 = [2, 'hello', True, 4, 0, 'se7en', 8, False, 6, 4]
random_list_2 = [5, 7, False, 2, 'six', 'hello', 9, 0, 6]
print('Первый список:', random_list_1)
print('Второй список:', random_list_2)

for element in random_list_2:
    if element in random_list_1:
        random_list_1.remove(element)

print('Результат:', random_list_1)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

num_list = [1, 5, 8, 6, 4, 9, 2, 3, 7, 6, 4, 3, 0, 2, 1]
new_num_list = []
for element in num_list:
    if element % 2 == 0:
        new_num_list.append(element / 4)
    else:
        new_num_list.append(element * 2)

print()
print('Список целых чисел:', num_list)
print('Результат:', new_num_list)
