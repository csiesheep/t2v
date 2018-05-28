#!/usr/bin/python
# -*- encoding: utf8 -*-

import csv
import optparse
import sys


__author__ = 'sheep'


def main(fname, output_fname, min_length):
    '''\
    %prog [options] <fname> <output_fname> <min_length>
    '''
    min_length = int(min_length)

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
                if len(xys) < min_length:
                    continue

                fo.write('"%s"\n' % '","'.join(line))
    return 0


if __name__ == '__main__':
    parser = optparse.OptionParser(usage=main.__doc__)
    options, args = parser.parse_args()

    if len(args) != 3:
        parser.print_help()
        sys.exit()

    sys.exit(main(*args))

