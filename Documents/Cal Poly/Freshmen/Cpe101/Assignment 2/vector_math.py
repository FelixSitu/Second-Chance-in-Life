import math
from utility import *

class Point():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        xeq = epsilon_equal(self.x,other.x)
        yeq = epsilon_equal(self.y,other.y)
        zeq = epsilon_equal(self.x,other.z)
        return xeq,yeq,zeq

class Vector():
    def __init__(self,xdir,ydir,zdir):
        self.xdir = xdir
        self.ydir = ydir
        self.zdir = zdir

    def __eq__(self, other):
        xdireq = epsilon_equal(self.xdir,other.xdir)
        ydireq = epsilon_equal(self.ydir,other.ydir)
        zdireq = epsilon_equal(self.zdir,other.zdir)
        return xdireq and ydireq and zdireq

class Ray():
    def __init__(self,pt,dir):
        self.pt = pt
        self.dir = dir

    def __eq__(self, other):
        pteq = epsilon_equal(self.pt,other.pt)
        direq = epsilon_equal(self.dir,other.dir)
        return pteq and direq

class Sphere():
    def __init__(self,center,radius):
        self.center = center
        self.radius = radius

    def __eq__(self, other):
        centereq = epsilon_equal(self.center,other.center)
        radiuseq = epsilon_equal(self.radius,other.radius)
        return centereq and radiuseq

def scale_vector(vector,scale):
    new_vec = Vector(vector.xdir,vector.ydir,vector.zdir)
    new_vec.xdir = new_vec.xdir * scale
    new_vec.ydir = new_vec.ydir * scale
    new_vec.zdir = new_vec.zdir * scale
    return Vector(new_vec.xdir, new_vec.ydir, new_vec.zdir)

def dot_vector(vector1,vector2):
    com1 = vector1.xdir * vector2.xdir
    com2 = vector1.ydir * vector2.ydir
    com3 = vector1.zdir * vector2.zdir
    return (com1 + com2 + com3)

def length_vector(vector):
   lengthX = (vector.xdir)**2
   lengthY = (vector.ydir)**2
   lengthZ = (vector.zdir)**2
   return math.sqrt(lengthX + lengthY + lengthZ)

def normalize_vector(vector):
    length = length_vector(vector)
    x1 = vector.xdir / length
    y1 = vector.ydir / length
    z1 = vector.zdir / length
    return Vector(x1,y1,z1)

def difference_point(point1,point2):
    x1 = point2.x - point1.x
    y1 = point2.y - point1.y
    z1 = point2.z - point1.z
    return x1 and y1 and z1

def difference_vector(vector1,vector2):
    x1 = vector2.xdir - vector1.xdir
    y1 = vector2.ydir - vector1.ydir
    z1 = vector2.zdir - vector1.zdir
    return Vector(x1,y1,z1)

def translate_point(point, vector):
    x1 = point.x + vector.xdir
    y1 = point.y + vector.ydir
    z1 = point.z + vector.zdir
    return Vector(x1,y1,z1)

def vector_from_to(from_point, to_point):
    vecX = to_point.x - from_point.x
    vecY = to_point.y - from_point.y
    vecZ = to_point.z - from_point.z
    return Vector(vecX,vecY,vecZ)