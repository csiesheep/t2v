#!/usr/bin/python
# -*- encoding: utf8 -*-

import datetime
from dateutil import parser as time_parser
import optparse
import os
import sys


__author__ = 'sheep'


def main(fname, output_fname):
    '''\
    %prog [options] <fname> <output_fname>
    '''
    id2locations = load_locations(fname)
    print len(id2locations)
    id2traj = segment_trajs(id2locations, output_fname, min_length=10, max_gap=45)
    return 0

def load_locations(fname):
    id2locations = {}
    i = 0
    j = 0
    with open(fname) as f:
        for line in f:
            i += 1
            if i % 1000000 == 0:
                print i

            tokens = line.strip().split(',')
            if tokens[4] != '2' and tokens[4] != '4':
                continue
            id_ = int(tokens[0])
            time = int(float(tokens[1]))
            x = float(tokens[2])
            y = float(tokens[3])

            j += 1

            if id_ not in id2locations:
                id2locations[id_] = [(time, x, y)]
                continue
            id2locations[id_].append((time, x, y))
    for id_, locations in id2locations.items():
        id2locations[id_] = sorted(locations)
    print i, j
    return id2locations

def segment_trajs(id2locations, output_fname, min_length=10, max_gap=30):
    id2trajs = {}
    count = 0
    ith = 0
    ids = set()
    with open(output_fname, 'w') as fo:
        for id_, locations in id2locations.items():
            id2trajs[id_] = []
            traj = []
            for time, x, y in locations:
                if len(traj) == 0:
                    traj.append((time, x, y))
                    continue

                if time - traj[-1][0] <= max_gap:
                    traj.append((time, x, y))
                    continue

                if len(traj) >= min_length:
                    ith += 1
                    count += len(traj)
                    id2 = "%d_%d" % (id_, ith)
                    if id2 in ids:
                        print id2
                    ids.add(id2)
                    fo.write("%s %s\n" % (id2, str(traj)))
                    traj = []
            if len(traj) >= min_length:
                ith += 1
                count += len(traj)
                id2 = "%d_%d" % (id_, ith)
                if id2 in ids:
                    print id2
                ids.add(id2)
                fo.write("%s %s\n" % (id2, str(traj)))
    print count
    return id2trajs



if __name__ == '__main__':
    parser = optparse.OptionParser(usage=main.__doc__)
    options, args = parser.parse_args()

    if len(args) != 2:
        parser.print_help()
        sys.exit()

    sys.exit(main(*args))

