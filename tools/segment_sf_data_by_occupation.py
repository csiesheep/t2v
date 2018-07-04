#!/usr/bin/python
# -*- encoding: utf8 -*-

import optparse
import os
import sys


__author__ = 'sheep'


def main(folder, output_folder):
    '''\
    %prog [options] <folder> <output_folder>
    '''
#   if os.path.exists(output_folder):
#       os.system("rm -r %s" % output_folder)
#   os.system("mkdir %s" % output_folder)

    id_ = 0
    gap = 45
    for ith, fname in enumerate(os.listdir(folder)):
        fpath = os.path.join(folder, fname)
        if fname.startswith("_") or fname == "README":
            continue
        id_ = segment(fpath, gap, output_folder, id_)


def segment(fpath, gap, output_folder, id_):
    traj = []
    pre_timestamp = None
    with open(fpath) as f:
        for line in f:
            tokens = line.strip().split(' ')
            if tokens[-2] == '1':
                pre_timestamp = None
                if len(traj) < 10:
                    traj = []
                    continue

                output_fpath = os.path.join(output_folder, ("%d.txt" % id_))
                with open(output_fpath, 'w') as fo:
                    for point in traj:
                        fo.write(point)
                print id_
                id_ += 1
                traj = []
                continue

            timestamp = int(tokens[-1])
            if pre_timestamp is None:
                traj.append(line)
                pre_timestamp = timestamp
                continue

            if (pre_timestamp - timestamp) <= gap:
                traj.append(line)
                pre_timestamp = timestamp
                continue

            if len(traj) >= 10:
                output_fpath = os.path.join(output_folder, ("%d.txt" % id_))
                with open(output_fpath, 'w') as fo:
                    for point in traj:
                        fo.write(point)
                print id_
                id_ += 1

            pre_timestamp = timestamp
            traj = [line]
    return id_

def get_time_intervals(fpath):
    pre_timestamp = None
    gaps = []
    with open(fpath) as f:
        for line in f:
            tokens = line.strip().split(' ')
            timestamp = int(tokens[-1])
            if pre_timestamp is None:
                pre_timestamp = timestamp
                continue

            gaps.append(pre_timestamp - timestamp)
            pre_timestamp = timestamp
    return sorted(gaps)


if __name__ == '__main__':
    parser = optparse.OptionParser(usage=main.__doc__)
    options, args = parser.parse_args()

    if len(args) != 2:
        parser.print_help()
        sys.exit()

    sys.exit(main(*args))

