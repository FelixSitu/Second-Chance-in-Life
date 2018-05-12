import math
from objects import *

def distance(p1,p2):
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    dsquared = dx**2+dy**2
    result = math.sqrt(dsquared)
    return result

def circle_overlap(c1,c2):
    #distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
    dist = distance(c1.center,c2.center)
    radiusSum = c1.radius + c2.radius #two circles will have same radius
    return dist <= radiusSum
