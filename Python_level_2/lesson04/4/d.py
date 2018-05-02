
import dis, socket

def func():

    #sock = socket.socket()

    v = 10
    print(v)

print(dis.dis(func))
ds = dis.Bytecode(func)

for i in ds:

    if i.opname == "LOAD_ATTR" and i.argval == "socket":

        print("We found socket")

