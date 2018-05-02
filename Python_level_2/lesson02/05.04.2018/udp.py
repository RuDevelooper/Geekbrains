#!/usr/bin/env python3

import socket
import pickle
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--ip", type = str, default = "127.0.0.1", help = "our ip")
parser.add_argument("--port", type = int, default = 7891, help = "our port")

args = parser.parse_args()

# <------------- args.ip, args.port

sock = socket.socket(
        family = socket.AF_INET,
        type = socket.SOCK_DGRAM,
        proto = 0)

sock.bind((args.ip, args.port))

data = sock.recv(1024)

print(data)

print(pickle.loads(data[4 : ]))

