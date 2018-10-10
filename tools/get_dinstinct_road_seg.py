#!/usr/bin/python
# -*- encoding: utf8 -*-

import sys
import optparse


__author__ = 'sheep'


def main(fname, output_fname):
    '''\
    %prog [options] <traj_fname> <output_fname>
    '''
    seg2count = {}
    with open(fname) as f:
        for line in f:
            line = line.strip()
            segs = line.split(' ')
            for seg in segs:
                if len(seg) == 0:
                    continue
                if seg not in seg2count:
                    seg2count[seg] = 1
                    continue
                seg2count[seg] += 1

    with open(output_fname, 'w') as fo:
#       fo.write('<unk>\n')
#       fo.write('<s>\n')
#       fo.write('</s>\n')
        for seg, count in sorted(seg2count.items(),
                                 key=lambda x:x[1],
                                 reverse=True):
            fo.write('%s\n' % seg)
    return 0


if __name__ == '__main__':
    parser = optparse.OptionParser(usage=main.__doc__)
    options, args = parser.parse_args()

    if len(args) != 2:
        parser.print_help()
        sys.exit()

    sys.exit(main(*args))

