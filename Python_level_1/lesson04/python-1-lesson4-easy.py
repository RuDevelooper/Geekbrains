# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

some_list = [1, 2, 4, 0]
square_list = [i ** 2 for i in some_list]
print(some_list, '-->', square_list)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruit_list_1 = ['яблоко', 'банан', 'апельсин', 'груша', 'мандарин', 'хурма']
fruit_list_2 = ['анис', 'груша', 'авокадо', 'манго', 'апельсин', 'ананас', 'банан']
common_fruit_list = [fruit for fruit in fruit_list_1 if fruit in fruit_list_2]
print(common_fruit_list)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

random_list = [9, 16, -8, 92, -9, -37, 45, 25, 68, 39]

filtered_list = [i for i in random_list if (i % 3 == 0) & (i > 0) & (i % 4 != 0)]
print(filtered_list)