#!/usr/bin/env python3

import argparse
import lib
import logging

logger = logging.getLogger('app')
parser = argparse.ArgumentParser()

parser.add_argument('host', help='Server IP-address', type=lib.is_host_correct)
parser.add_argument('port', help='TCP-port 1024 <= port <= 65535 (default=7777)', default=7777,
                    type=lib.is_port_correct, nargs='?')

args = parser.parse_args()
logger.info('Start client. Connected to: %s, Port: %s' % (args.host, args.port))


lib.CClient(args.host, args.port)
