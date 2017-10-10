#! /usr/bin/env python

import logging
import argparse
from engine import Driver, run_engine

# Setting logger
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

fmt = logging.Formatter(datefmt="%H:%M:%S",
                        fmt='%(asctime)s %(levelname)-8s: %(name)s: %(message)s')
sh = logging.StreamHandler()
sh.setFormatter(fmt)
log.addHandler(sh)
log.setLevel(logging.INFO)


def parse_cmds():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action='store_true', help="Enables verbose logging")
    parser.add_argument("-c", "--chrome", action='store_true', help="Runs on chrome driver")
    parser.add_argument("-s", "--firefox", action='store_true', help="Runs on firefox driver")
    parser.add_argument("-p", "--path",help="Driver location path")
    parsed_args = parser.parse_args()
    args = []
    kwargs = {}
    if parsed_args.verbose:
        args.append('logLevel')
        kwargs['logLevel'] = logging.DEBUG
    if parsed_args.chrome:
        args.append('driver')
        kwargs['driver'] = Driver.chrome
    if parsed_args.firefox:
        args.append('driver')
        kwargs['driver'] = Driver.firefox
    if parsed_args.path:
        args.append('path')
        kwargs['path'] = parsed_args.path
    run_engine(args, kwargs)

if __name__ == '__main__':
    parse_cmds()