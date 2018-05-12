import math


def is_even(x):
    return x % 2 == 0


def is_an_interval(x, x1, x2):
    #interval (x1,x2]
    return x1 < x <= x2
