#!/usr/bin/python
# -*- encoding: utf8 -*-

import optparse
import sys


__author__ = 'sheep'


def main(fname, output_fname):
    '''\
    %prog [options] <fname> <output_fname>
    '''
    steps = 0.25
    with open(fname, 'r') as f:
        with open(output_fname, 'w') as fo:
            for line in f:
                _, traj = line.split(' ', 1)
                traj = eval(traj)
                destinations = []
                for i in range(1, 4):
                    ith = int(len(traj) * steps * i)
                    destinations.append(traj[ith][-2:])
                destinations.append(traj[-1][-2:])
                fo.write("%s\n" % str(destinations))
    return 0


if __name__ == '__main__':
    parser = optparse.OptionParser(usage=main.__doc__)
    options, args = parser.parse_args()

    if len(args) != 2:
        parser.print_help()
        sys.exit()

    sys.exit(main(*args))

