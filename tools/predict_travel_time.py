#!/usr/bin/python
# -*- encoding: utf8 -*-

import sys
import optparse
from sklearn import cross_validation, linear_model


__author__ = 'sheep'


def main(vec_fname, time_fname):
    '''\
    %prog [options]
    '''
    X, y = load(vec_fname, time_fname)
    regr = linear_model.LinearRegression()
    for k in [1000, 2000, 5000, 10000, 50000, 100000]:
        scores = cross_validation.cross_val_score(regr, X[:k], y[:k], scoring='neg_mean_squared_error', cv=5,)
        print k
        print scores
        print scores.mean()

    return 0

def load(vec_fname, time_fname):
    X = []
    y = []
    with open(vec_fname) as f:
        for line in f:
            vec = map(float, line.strip().split(' '))
            X.append(vec)
    with open(time_fname) as f:
        for line in f:
            y.append(int(line))
    print len(X), len(y)
    assert(len(X) == len(y))
    return X, y


if __name__ == '__main__':
    parser = optparse.OptionParser(usage=main.__doc__)
    options, args = parser.parse_args()

    if len(args) != 2:
        parser.print_help()
        sys.exit()

    sys.exit(main(*args))

