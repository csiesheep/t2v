#!/usr/bin/python
# -*- encoding: utf8 -*-

import sys
import optparse


__author__ = 'sheep'


def main(fname):
    '''\
    %prog [options]
    '''
    min_x = 10000
    min_y = 10000
    max_x = -10000
    max_y = -10000
#   with open(fname) as f:
#       for line in f:
#           line = line.strip()
#           tokens = line.split(',')
#           if tokens[4] != '2' and tokens[4] != '4':
#               continue
#           x, y = float(tokens[2]), float(tokens[3])

#           if x > max_x:
#               max_x = x
#           if x < min_x:
#               min_x = x
#           if y > max_y:
#               max_y = y
#           if y < min_y:
#               min_y = y
#       print "x", min_x, max_x
#       print "y", min_y, max_y

#   with open(fname) as f:
#       for line in f:
#           tokens = line.split(' ', 1)
#           traj = eval(tokens[1])
#           for _, x, y in traj:
#               if x > max_x:
#                   max_x = x
#               if x < min_x:
#                   min_x = x
#               if y > max_y:
#                   max_y = y
#               if y < min_y:
#                   min_y = y
#       print "x", min_x, max_x
#       print "y", min_y, max_y
    min_y = 35.28
    max_y = 36.41
    min_x = 139.07
    max_x = 140.51
    i = 0
    xc = 0
    yc = 0
    txc = 0
    tyc = 0
    with open(fname) as f:
        for line in f:
            tokens = line.split(' ', 1)
            traj = eval(tokens[1])
            for _, x, y in traj:
                if x > max_x or x < min_x:
                    xc += 1
                if y > max_y or y < min_y:
                    yc += 1
                i += 1
            for _, x, y in traj:
                if x > max_x or x < min_x:
                    txc += 1
                    break
            for _, x, y in traj:
                if y > max_y or y < min_y:
                    tyc += 1
                    break
        print i, xc, yc
        print txc, tyc
        print float(xc)/i
        print float(yc)/i
    return 0


if __name__ == '__main__':
    parser = optparse.OptionParser(usage=main.__doc__)
    options, args = parser.parse_args()

    if len(args) != 1:
        parser.print_help()
        sys.exit()

    sys.exit(main(*args))

