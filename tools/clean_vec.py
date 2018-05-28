#!/usr/bin/python
# -*- encoding: utf8 -*-

import sys
import optparse


__author__ = 'sheep'


def main(fname, output_fname):
    '''\
    %prog [options] <fname> <output_fname>
    '''
    with open(fname) as f:
        with open(output_fname, 'w') as fo:
            first = True
            for line in f:
                if first:
                    first = False
                    continue

                if line.startswith('</s>'):
                    continue
                else:
                    fo.write(line)
    return 0


if __name__ == '__main__':
    parser = optparse.OptionParser(usage=main.__doc__)
    options, args = parser.parse_args()

    if len(args) != 2:
        parser.print_help()
        sys.exit()

    sys.exit(main(*args))

