import math
from point import *

def are_positive(lst):
    nlst = list()
    for ent in lst:
        if ent > 0:
            nlst.append(ent)
    return nlst

def are_greater_than(lst,n):
    nlst = list()
    for ent in lst:
        if ent > n:
            nlst.append(ent)
    return nlst

def are_in_first_quadrant(number):
    nlst = list()
    for idx in number:
        x1 = idx.x
        y1 = idx.y
        if x1 > 0 and y1 > 0:
            nlst.append(idx) # idx is already a point
    return nlst