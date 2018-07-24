#!/usr/bin/python
# -*- encoding: utf8 -*-

import csv
import optparse
import sys


__author__ = 'sheep'


def main(fname, output_fname1, output_fname2):
    '''\
    %prog [options] <fname> <output_fname1> <output_fname2>
    '''
    with open(fname, 'r') as f:
        with open(output_fname1, 'w') as fo1:
            with open(output_fname2, 'w') as fo2:
                for line in f:
                    tokens = line.split(' ', 1)
                    id_ = tokens[0]
                    xys = eval(tokens[1])
                    xys1 = xys[:len(xys)/2]
                    fo1.write('%s %s\n' % (id_, str(xys1)))
                    xys2 = xys[len(xys)/2:]
                    fo2.write('%s %s\n' % (id_, str(xys2)))
    return 0


if __name__ == '__main__':
    parser = optparse.OptionParser(usage=main.__doc__)
    options, args = parser.parse_args()

    if len(args) != 3:
        parser.print_help()
        sys.exit()

    sys.exit(main(*args))

