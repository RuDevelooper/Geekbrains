# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import hw05_easy as easy

while True:
    try:
        answer = int(input('''1. Перейти в папку
2. Просмотреть содержимое текущей папки
3. Удалить папку
4. Создать папку
5. На уровень вверх
6. Выход
-------------------
Выберите действие: '''))
    except ValueError:
        print('\nВведите число от 1 до 6\n')
        continue

    if answer == 1:
        easy.ch_dir()

    elif answer == 2:
        easy.list_dir()

    elif answer == 3:
        easy.rem_dir()

    elif answer == 4:
        easy.mk_dir()

    elif answer == 5:
        easy.level_up()

    elif answer == 6:
        break
    else:
        print('\nВведите число от 1 до 6\n')