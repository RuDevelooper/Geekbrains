# import my_game_lib as gl
#
# result = gl.pow(2, 2)
# print(result)
# result = pow(2, 2)
# print(result)

# from my_game_lib import generate_person
#
# print(pow(2, 2))

# import lib.test
#
# import sys
# for name in sys.path:
#     print(name)

# print(os.name)
# print(os.getcwd())
# print(dir(os))

# dir_path = os.path.join(os.getcwd(), 'test')
# print(dir_path)
#
# try:
#     os.mkdir(dir_path)
# except FileExistsError:
#     print('РљР°С‚Р°Р»РѕРі СѓР¶Рµ СЃСѓС‰РµС‚СЃРІСѓРµС‚!')

import sys


# for key in sys.argv:
#     if key == 'help':
#         print('Р’С‹ РјРѕР¶РµС‚Рµ СѓРєР°Р·Р°С‚СЊ Hello!')
# def help():
#     print('Р­С‚Р° РїСЂРѕРіСЂР°РјРјР° РѕР±С‰РµРЅРёСЏ, РЅР°РїРёС€Рё РїСЂРёРІРµС‚!')
#
#
# def hello():
#     print('Р С‚РµР±Рµ РїСЂРёРІРµС‚!')
#
# try:
#     key = sys.argv[1]
# except IndexError:
#     help()

try:
    surname = sys.argv[1]
    name = sys.argv[2]
    middle_name = sys.argv[3]
except:
    print('Р¤ Р Рћ')

print(surname.title(), name.title(), middle_name.title())