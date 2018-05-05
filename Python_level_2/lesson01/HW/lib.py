import json
import socket
import time
import argparse
import logging
import ipaddress


class CBase:

    def __init__(self, sock):
        self.__sock = sock

    def send(self, data):
        data_json = json.dumps(data)
        data_buf = data_json.encode()
        self.__sock.send(data_buf)
        print('Send:', data)

    def recv(self):
        data_buf = self.__sock.recv(1024)
        data_json = data_buf.decode()
        data = json.loads(data_json)

        return data


class CClient(CBase):

    def __init__(self, host, port):
        sock = socket.socket()
        sock.connect((host, port))
        print('Connected to', host)
        super().__init__(sock)

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
        print(self.recv())


class CServer(CBase):

    def __init__(self, port, listening_host):
        sock = socket.socket()
        sock.bind((listening_host, port))
        sock.listen(5)

        while True:
            fd, addr = sock.accept()
            super().__init__(fd)
            print('Missage from', addr[0])
            self.__response(self.recv())

    def __response(self, data):
        action = {
            # 'authenticate': self.__auth()
            'presence': self.__confirmation
            # 'msg': ...
            # 'quit': self.__quit()
        }
        if 'action' in data:
            action.get(data.get('action'))()

    def __confirmation(self):
        print('Presence missage is accepted.')
        confirm_missage = {
            'response': 'YES'
        }
        self.send(confirm_missage)
        print('Confirmation sent.')


def is_host_correct(host):
    try:
        ipaddress.ip_address(host)
    except Exception:
        raise argparse.ArgumentTypeError('IP-addres is not correct!')
    else:
        return host


def is_port_correct(port):
    try:
        int_port = int(port)
    except Exception:
        raise argparse.ArgumentTypeError('TCP-port must be Integer and 1024 <= TCP-port <= 65535')
    else:
        if 1024 <= int_port <= 65535:
            return int_port
        else:
            raise argparse.ArgumentTypeError('1024 <= TCP-port <= 65535')
