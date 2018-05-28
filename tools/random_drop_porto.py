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
            spamreader = csv.reader(f, delimiter=',', quotechar='"')
            first = True
            for line in spamreader:
                if first:
                    first = False
                    fo.write('"%s"\n' % '","'.join(line))
                    continue

                xys = eval(line[-1])
                new_xys = drop(xys, drop_ratio)
                line[-1] = str(new_xys)
                fo.write('"%s"\n' % '","'.join(line))
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

