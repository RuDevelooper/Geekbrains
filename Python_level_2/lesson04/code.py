import dis
import socket

def func():
    sock = socket.socket()
    v = 20
    print(v)

print(dis.dis(func))
ds = dis.Bytecode(func)

for i in ds:
    if i.opname == 'LOAD_ATTR' and i.argval == 'socket':
        print('we found socket')

# SQL
# Таблица (отношение)
# Поле (столбец)
# Ключи (первичный, внешний)
# Связи между таблицами
#     Один к одному
#     Один ко многим
#     Многие ко многим
# Транзакция

# CREATE TABLE
# ALTER TABLE
# DROP TABLE
# SELECT
# INSERT
# UPDATE
# DELETE











