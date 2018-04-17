#!/usr/bin/env python3

import argparse
import lib


parser = argparse.ArgumentParser()
parser.add_argument('host', help='Server address')
parser.add_argument('port', help='Port (default=7777)', default=7777, nargs='?')
args = parser.parse_args()

print(args.host, args.port)

lib.CClient(args.host, args.port)


