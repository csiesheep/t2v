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
                _, traj = line.split(' ', 1)
                traj = eval(traj)
                time = int(traj[-1][0]) - int(traj[0][0])
                fo.write('%d\n' % time)
    return 0


if __name__ == '__main__':
    parser = optparse.OptionParser(usage=main.__doc__)
    options, args = parser.parse_args()

    if len(args) != 2:
        parser.print_help()
        sys.exit()

    sys.exit(main(*args))

