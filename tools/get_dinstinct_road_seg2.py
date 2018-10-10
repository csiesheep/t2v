#!/usr/bin/python
# -*- encoding: utf8 -*-

import sys
import optparse


__author__ = 'sheep'


def main(fname, output_fname):
    '''\
    %prog [options] <w2v_fname> <output_fname>
    '''
    seg2count = {}
    with open(fname) as f:
        with open(output_fname, 'w') as fo:
            for line in f:
                line = line.strip()
                tokens = line.split(' ')
                if len(tokens) == 2:
                    continue
                fo.write('%s\n' % tokens[0])
    return 0


if __name__ == '__main__':
    parser = optparse.OptionParser(usage=main.__doc__)
    options, args = parser.parse_args()

    if len(args) != 2:
        parser.print_help()
        sys.exit()

    sys.exit(main(*args))

