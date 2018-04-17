# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.


import os


def mk_dirs():
    for i in range(9):
        os.mkdir(os.path.join(os.getcwd(), 'dir_' + str(i + 1)))
        print('Папка %s создана' % ('dir_' + str(i + 1)))


# И второй скрипт, удаляющий эти папки.

def rem_dirs():
    for i in range(9):
        os.rmdir('dir_' + str(i + 1))
        print('Папка %s удалена' % ('dir_' + str(i + 1)))


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def show_dirs(path=os.getcwd()):
    if os.listdir(path) != []:
        print('\nТекущая директория содержит:')
        for i in os.listdir(path):
            if os.path.isdir(i):
                print(i)
    else:
        print('\nТекущая директория пуста.')


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


# os.path.join(os.getcwd(), dir_name)


def copy_file(path=__file__):
    file = open(path, 'r', encoding='utf-8')
    str = file.read()
    file.close()
    file = open('copy_' + os.path.basename(path), 'w', encoding='utf-8')
    file.write(str)
    file.close()


# вызовы функций и демонстрация работы программы

if __name__ == '__main__':
    mk_dirs()

    show_dirs()

    rem_dirs()


# Модули для NORMAL

def ch_dir():
    try:
        os.chdir(os.path.join(os.getcwd(), input('\nВведите имя папки: ')))
    except FileNotFoundError:
        print('\nНевозможно перейти\n')
    else:
        print('\nУспешно перешел.\n')


def list_dir():
    if os.listdir(os.getcwd()) != []:
        print('\nТекущая директория содержит:')
        for i in os.listdir(os.getcwd()):
            print(i)
        print()
    else:
        print('\nТекущая директория пуста.\n')


def rem_dir():
    try:
        os.rmdir(os.path.join(os.getcwd(), input('\nВведите имя папки: ')))

    except FileNotFoundError:
        print('\nНевозможно удалить папку которой не существует.\n')

    else:
        print('\nПапка успешно удалена\n')


def mk_dir():
    try:
        os.mkdir(os.path.join(os.getcwd(), input('\nВведите имя папки: ')))
    except FileExistsError:
        print('\nПапка уже существует.\n')
    else:
        print('\nПапка успешно создана\n')


def level_up():
    os.chdir(os.path.split(os.getcwd())[0])
    print('Перешел на один уровень вверх.\n')
