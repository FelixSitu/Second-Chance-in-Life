import math
from point import *


def sum(number):
    result = 0
    for idx in number:
        result += idx
    return result

def sum2(lst):
    acc = 0
    idx = 0
    while idx < len(lst):
        acc +=lst[idx]
        idx += 1
    return acc

def index_of_smallest(lst):
    if len(lst) > 0:
        min = lst[0]
        #sidx = 0
        for idx in range(1,len(lst),1):
            if min > lst[idx]:
                min = lst[idx]
                #sidx = idx
        return idx
    else:
        return None

def distance(pt1,pt2):
    length = math.sqrt((pt2.x - pt1.x)**2 + (pt2.y - pt1.y)**2 + (pt2.z - pt1.z)**2)
    return length

def get_distances(pt_lists):
    distances = list()
    for pt in pt_lists:
        distances.append(distance(Point(0,0),pt))
    return distances

def nearest_origin(pts):
    dists = get_distances(pts)
    return index_of_smallest(dists)
