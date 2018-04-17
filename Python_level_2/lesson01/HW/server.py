#!/usr/bin/env python3

import socket
import argparse
import lib

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--port', help='TCP-port(default=7777)', default=7777, nargs='?')
parser.add_argument('-a', '--addr', help='Listening IP (default=all)', default='', nargs='?')
args = parser.parse_args()

serv = lib.CServer(args.port, args.addr)

print(dir(serv))
# server_sock = socket.socket(
#     family=socket.AF_INET,
#     type=socket.SOCK_STREAM,
#     proto=0)
#
# server_sock.bind(('', 7777))
#
# server_sock.listen(5)
#
while True:
    sock, addr = serv.sock.accept()
    print('Подключение от', type(addr))

    lib.presence_for_server(sock)

    sock.close()
