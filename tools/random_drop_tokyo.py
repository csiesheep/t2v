#!/usr/bin/python
# -*- encoding: utf8 -*-

import csv
import optparse
import random
import sys


__author__ = 'sheep'


def main(fname, output_fname, drop_ratio):
    '''\
    %prog [options] <fname> <output_fname> <drop_ratio>
    '''
    drop_ratio = float(drop_ratio)

    with open(fname, 'r') as f:
        with open(output_fname, 'w') as fo:
            for line in f:
                tokens = line.split(' ', 1)
                id_ = tokens[0]
                xys = eval(tokens[1])
                new_xys = drop(xys, drop_ratio)
                fo.write('%s %s\n' % (id_, str(new_xys)))
    return 0

def drop(xys, drop_ratio):
    new_xys = []
    for xy in xys:
        if random.random() > drop_ratio:
            new_xys.append(xy)
    return new_xys


if __name__ == '__main__':
    parser = optparse.OptionParser(usage=main.__doc__)
    options, args = parser.parse_args()

    if len(args) != 3:
        parser.print_help()
        sys.exit()

    sys.exit(main(*args))

