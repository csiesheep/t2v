#!/usr/bin/python
# -*- encoding: utf8 -*-

import math
import optparse
import sys


__author__ = 'sheep'


def main(traj_vec_fname1, traj_vec_fname2, traj_fname1, traj_fname2):
    '''\
    %prog [options] <traj_vec_fname1> <traj_vec_fname2> <traj_fname1> <traj_fname2>
    '''
    traj2vec1 = load(traj_vec_fname1)
    traj2vec2 = load(traj_vec_fname2)
    traj2len1 = load_length(traj_fname1)
    traj2len2 = load_length(traj_fname2)

    total_rank = 0.0
    for id_, vec in traj2vec2.items():
        if traj2len1[id_] == 1 or traj2len2[id_] == 1:
            continue

        r = rank(id_, vec, traj2vec1, traj2len1)
        total_rank += r
        if r > 5:
            print id_, r, total_rank / (id_+1), traj2len1[id_], traj2len2[id_]
    print total_rank / len(traj2vec2)

    return 0

def rank(id_, vec, traj2vec, traj2length):
    traj2score = []
    for id2, vec2 in traj2vec.items():
        if traj2length[id2] == 0:
            continue
        score = sum([(v1-v2)*(v1-v2) for v1, v2 in zip(vec, vec2)])
        traj2score.append((score, id2))
    traj2score = sorted(traj2score)
    for ith, (_, id2) in enumerate(traj2score):
        if id2 == id_:
            return ith

def load(fname):
    traj2vec = {}
    with open(fname) as f:
        ith = 0
        for line in f:
            line = line.strip()
            vec = map(float, line.split(' '))
            traj2vec[ith] = vec
            ith += 1
    return traj2vec

def load_length(fname):
    traj2length = {}
    with open(fname) as f:
        ith = 0
        for line in f:
            traj2length[ith] = len(line.strip().split(' '))
            ith += 1
    return traj2length


if __name__ == '__main__':
    parser = optparse.OptionParser(usage=main.__doc__)
    options, args = parser.parse_args()

    if len(args) != 4:
        parser.print_help()
        sys.exit()

    sys.exit(main(*args))

