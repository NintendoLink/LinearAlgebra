# python 3.6.4
# encoding: utf-8
EPSILON = 1e-8

def is_zero(x):
    return abs(x) < EPSILON

def is_equal(x,y):
    return abs(x - y) <= EPSILON