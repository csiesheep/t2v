#!/usr/bin/python
# -*- encoding: utf8 -*-

import optparse
import random
import sys


__author__ = 'sheep'


def main(traj_fname, output_fname, number):
    '''\
    %prog [options] <traj_fname> <output_fname> <number>
    '''
    number = int(number)
    count = get_traj_count(traj_fname)
    print count

    selected = set()
    while len(selected) < number:
        selected.add(random.randint(1, count-1))
    print len(selected)
    selected.add(0)

    with open(traj_fname, 'r') as f:
        with open(output_fname, 'w') as fo:
            ith = 0
            for line in f:
                if ith in selected:
                    fo.write(line)
                ith += 1
    return 0

def get_traj_count(fname):
    count = 0
    with open(fname, 'r') as f:
        for line in f:
            count += 1
    return count-1


if __name__ == '__main__':
    parser = optparse.OptionParser(usage=main.__doc__)
    options, args = parser.parse_args()

    if len(args) != 3:
        parser.print_help()
        sys.exit()

    sys.exit(main(*args))

