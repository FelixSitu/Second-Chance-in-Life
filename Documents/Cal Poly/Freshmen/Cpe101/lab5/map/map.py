import math
from point import *

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        xeq = epsilon_equal(self.x,other.x)
        yeq = epsilon_equal(self.y,other.y)
        return xeq,yeq,zeq

"""def square_all(number):
    for idx in range(0,len(number),1):
        number[idx] = number[idx]**2
    return number"""

def square_all(lst):
    nlst = list()
    for num in lst:
        num = num**2
        nlst.append(num)
    return nlst

"""def add_n_all(number, n):
    for idx in range(0,len(number),1):
        number[idx] += n
    return number"""

def add_n_all(number,n):
    nlst = list()
    for num in number:
        result = num + n
        nlst.append(result)
    return nlst

def distance_all(lst):
    nlst = list()
    for point in lst:
        x1 = point.x
        y1 = point.y
        nlst.append(math.sqrt(x1**2 + y1**2))
    return nlst