import json
import socket
import time


class CBase:

    def __init__(self, sock):
        self.__sock = sock

    def send(self, data):

        data_json = json.dumps(data)
        data_buf = data_json.encode()
        self.__sock.send(data_buf)

    def recv(self):

        data_buf = self.__sock.recv(1024)
        data_json = data_buf.decode()
        data = json.loads(data_json)

        return data

    def is_host_correct(self, host):
        if re.match('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', host):
            return host
        else:
            print('IP-адрес введен некорректно')
            sys.exit()


class CClient(CBase):

    def __init__(self, host, port):
        sock = socket.socket()
        sock.connect((host, port))
        super().__init__(sock)

        print('Connected to', host)

        missage_of_presence = \
            {
                'action': 'presence',
                'time': time.clock(),
                'user': {
                    'account_name': 'admin',
                    'status': 'GOOD'
                }
            }

        self.send(missage_of_presence)


class CServer(CBase):

    def __init__(self, port, listening_host):
        sock = socket.socket()
        sock.bind((listening_host, port))
        sock.listen(5)
        super().__init__(sock)

    @property
    def sock(self):
        return sock

    # def presence_for_server(sock):
    #     buf = sock.recv(1024)
    #     buf_json = buf.decode()
    #     mis_from_client = json.loads(buf_json)
    #
    #     print(*mis_from_client)
    #
    #     mis = \
    #         {
    #             'action': 'probe',
    #             'time': time.clock()
    #         }
    #
    #     missage_json = json.dumps(mis)
    #     buf = missage_json.encode()
    #     answ = \
    #         {
    #
    #         }


# parser = argparse.ArgumentParser()
# parser.add_argument('--host', help = 'server address', required=True)
# args = parser.parse_args()


# def is_host_correct(host):
#     if re.match('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', host):
#         return host
#     else:
#         print('IP-адрес введен некорректно')
#         sys.exit()


# def start_client(sock):
#     # try:
#     #     addr = sys.argv[1]
#     # except IndexError:
#     #     print('Адрес сервера не задан.')
#     #     sys.exit()
#     # else:
#     #     check_host(addr)
#     #     try:
#     #         port = sys.argv[2]
#     #     except IndexError:
#     #         port = 7777
#     #         print('Будет использован порт: 7777')
#     #     print('Соединение с %s:%s' % (addr, port))
#     #     try:
#     #         sock.connect((addr, port))
#     #     except Exception:
#     #         print('Сервер не найден')
#     #         sys.exit()
#
#     parser = argparse.ArgumentParser()
#     parser.add_argument('host', help='Server address', type=str)
#     parser.add_argument('port', help='Port (default=7777)', default=7777, nargs='?')
#     args = parser.parse_args()
#     print(args, type(args.host))


# def start_server(sock):
#     try:
#         param = sys.argv[1]
#     except IndexError:
#         print('Для работы будет использован TCP-порт: 7777, слушать будем все хосты')
#     else:
#         try:
#             arg = sys.argv[2]
#         except IndexError:
#             print('Параметры командной строки:'
#                   '-p <port> - TCP-порт для работы (по умолчанию использует порт 7777)'
#                   '-a <addr> - IP-адрес для прослушивания (по умолчанию слушает все доступные адреса)')
#             sys.exit()
#
#     server_sock.bind(('', 7777))


def presence_for_server(sock):
    buf = sock.recv(1024)
    buf_json = buf.decode()
    mis_from_client = json.loads(buf_json)

    print(*mis_from_client)

    mis = \
        {
            'action': 'probe',
            'time': time.clock()
        }

    missage_json = json.dumps(mis)
    buf = missage_json.encode()
    answ = \
        {

        }

    # sock.send(buf)
    # result_buf = sock.recv(1024)
    #
    # result = json.loads(result_buf.decode())
    #
    # print(result)
    #
    # return result

#
# def presence_by_client(sock):
#     req = \
#         {
#             'action': 'presence',
#             'time': time.clock(),
#             'user': {
#                 'account_name': 'admin',
#                 'status': 'GOOD'
#             }
#         }
#
#     req_json = json.dumps(req)
#     buf = req_json.encode()
#     sock.send(buf)
