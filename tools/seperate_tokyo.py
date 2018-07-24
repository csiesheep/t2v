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
                    line = line.strip()
                    tokens = line.split(' ', 1)
                    traj = eval(tokens[1])
                    traj1, traj2= separate(traj)
                    fo1.write('%s %s\n' % (tokens[0], traj1))
                    fo2.write('%s %s\n' % (tokens[0], traj2))
    return 0

def separate(traj):
    traj1 = []
    traj2 = []
    for i, d in enumerate(traj):
        if i % 2 == 0:
            traj1.append(d)
        else:
            traj2.append(d)
    return traj1, traj2


if __name__ == '__main__':
    parser = optparse.OptionParser(usage=main.__doc__)
    options, args = parser.parse_args()

    if len(args) != 3:
        parser.print_help()
        sys.exit()

    sys.exit(main(*args))

