#!/usr/bin/python
# -*- encoding: utf8 -*-

import datetime
import optparse
import os
import sys


__author__ = 'sheep'


def main(folder):
    '''\
    %prog [options] <folder>
    '''
    stats = {}
    for fname in os.listdir(folder):
        fpath = os.path.join(folder, fname)
        with open(fpath) as f:
            for line in f:
                traj = eval(line)
                if len(traj) not in stats:
                    stats[len(traj)] = 1
                    continue
                stats[len(traj)] += 1
    for len_, count in sorted(stats.items()):
        print len_, count
    return 0


if __name__ == '__main__':
    parser = optparse.OptionParser(usage=main.__doc__)
    options, args = parser.parse_args()

    if len(args) != 1:
        parser.print_help()
        sys.exit()

    sys.exit(main(*args))

