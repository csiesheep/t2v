#!/usr/bin/python
# -*- encoding: utf8 -*-

import datetime
from dateutil import parser as time_parser
import optparse
import os
import sys


__author__ = 'sheep'


def main(folder, output_fname):
    '''\
    %prog [options] <folder> <output_fname>
    '''
    trasform(folder, output_fname)
    return 0

def trasform(folder, output_fname):
    base = time_parser.parse("2016-12-16 03:00:00")
    with open(output_fname, 'w') as fo:
        for fname in sorted(os.listdir(folder)):
            fpath = os.path.join(folder, fname)
            with open(fpath) as f:
                for line in f:
                    tokens = line.strip().split(',')
                    time = time_parser.parse(tokens[1])
                    time = (time - base).total_seconds()
                    tokens[1] = str(time)
                    fo.write("%s\n" % ','.join(tokens))


if __name__ == '__main__':
    parser = optparse.OptionParser(usage=main.__doc__)
    options, args = parser.parse_args()

    if len(args) != 2:
        parser.print_help()
        sys.exit()

    sys.exit(main(*args))

