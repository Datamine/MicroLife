#!/usr/bin/python3

import logging
logging.basicConfig(filename='MicroLife.log',level=logging.DEBUG)

def log(string, config='print'):
    """
    logs a message, either to the command line or to a logfile
    """

    if config == 'print':
        print(string)
    elif config == 'file':
        logging.info(string)
    else:
        raise ValueError("Unrecognized configuration option: {}".format(config))


