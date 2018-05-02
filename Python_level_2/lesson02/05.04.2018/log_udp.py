#!/usr/bin/env python3

import logging
import logging.handlers

logger = logging.getLogger("test_log")

fn = logging.handlers.DatagramHandler("127.0.0.1", 7891)
fn.setLevel(logging.DEBUG)

logger.addHandler(fn)
logger.setLevel(logging.DEBUG)

##########################

logger.info("TODO")

