#!/usr/bin/python
# -*- encoding: utf8 -*-

import csv
import optparse
import sys


__author__ = 'sheep'


def main(fname, output_fname):
    '''\
    %prog [options] <fname> <output_fname>
    '''
    with open(fname, 'r') as f:
        with open(output_fname, 'w') as fo:
            for line in f:
                traj = eval(line)
                traj = [[x, y] for x, y, z in traj]
                fo.write('%s\n' % traj)
    return 0


if __name__ == '__main__':
    parser = optparse.OptionParser(usage=main.__doc__)
    options, args = parser.parse_args()

    if len(args) != 2:
        parser.print_help()
        sys.exit()

    sys.exit(main(*args))

