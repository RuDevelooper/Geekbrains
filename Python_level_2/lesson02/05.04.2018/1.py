#!/usr/bin/env python3

import argparse

# dir /?
# ./client.py --port 7777 --host 192.0.0.1

parser = argparse.ArgumentParser()
parser.add_argument("--host", help = "server address", required = True)
args = parser.parse_args()

# sys.argv

print(args.host)

