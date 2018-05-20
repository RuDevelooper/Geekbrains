#!/usr/bin/env python3

import argparse
import lib
import logging

logger = logging.getLogger('app')

logger.info('start server')
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--port', help='TCP-port 1024 < port < 65535 (default=7777)',
                     default=7777, type=lib.is_port_correct, nargs='?')
parser.add_argument('-a', '--addr', help='Listening IP (default=all)',
                    default='0.0.0.0', type=lib.is_host_correct,  nargs='?')
args = parser.parse_args()
logger.info('Start server for listening IP: %s, Port: %s' % (args.addr, args.port))

lib.CServer(args.port, args.addr)


