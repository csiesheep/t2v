#!/usr/bin/python
# -*- encoding: utf8 -*-

import sys
import optparse
from sklearn import cross_validation, linear_model


__author__ = 'sheep'


def main(vec_fname, dest_fname):
    '''\
    %prog [options]
    '''
    X, ys = load(vec_fname, dest_fname)
    regr = linear_model.LinearRegression()

    ys_scores = []
    for ith, y in enumerate(ys):
        scores = cross_validation.cross_val_score(regr, X, y, scoring='neg_mean_squared_error', cv=5,)
        print scores
        print scores.mean()
        ys_scores.append(scores.mean())

    for ith in range(len(ys_scores)/2):
        print ith, float(ys_scores[ith*2]), float(ys_scores[ith*2+1]), float(ys_scores[ith*2] + ys_scores[ith*2+1])/2

    return 0

def load(vec_fname, dest_fname):
    X = []
    ys = []
    with open(vec_fname) as f:
        for line in f:
            vec = map(float, line.strip().split(' '))
            X.append(vec)
    with open(dest_fname) as f:
        for line in f:
            dests = eval(line)
            if len(ys) == 0:
                for xy in dests:
                    ys.append([])
                    ys.append([])
            for ith, (x, y) in enumerate(dests):
                ys[ith*2].append(x)
                ys[ith*2+1].append(y)
    print len(X), len(ys[0])
    assert(len(X) == len(ys[0]))
    return X, ys


if __name__ == '__main__':
    parser = optparse.OptionParser(usage=main.__doc__)
    options, args = parser.parse_args()

    if len(args) != 2:
        parser.print_help()
        sys.exit()

    sys.exit(main(*args))

