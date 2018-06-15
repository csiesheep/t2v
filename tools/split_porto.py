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
                spamreader = csv.reader(f, delimiter=',', quotechar='"')
                first = True
                for line in spamreader:
                    if first:
                        first = False
                        fo1.write('"%s"\n' % '","'.join(line))
                        fo2.write('"%s"\n' % '","'.join(line))
                        continue

                    xys = eval(line[-1])
                    line[-1] = str(xys[:len(xys)/2])
                    fo1.write('"%s"\n' % '","'.join(line))
                    line[-1] = str(xys[len(xys)/2:])
                    fo2.write('"%s"\n' % '","'.join(line))
    return 0


if __name__ == '__main__':
    parser = optparse.OptionParser(usage=main.__doc__)
    options, args = parser.parse_args()

    if len(args) != 3:
        parser.print_help()
        sys.exit()

    sys.exit(main(*args))

