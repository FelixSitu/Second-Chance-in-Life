from utility import *

class Point():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        xeq = epsilon_equal(self.x,other.x)
        yeq = epsilon_equal(self.y,other.y)
        zeq = epsilon_equal(self.z,other.z)
        return xeq and yeq and zeq

    def __repr__(self):
        return 'point,x={0},y={1},z={2}'.format(self.x,self.y,self.z)

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

    def __repr__(self):
        return 'vector,xdir={0},ydir={1},zdir={2}'.format(self.xdir,self.ydir,self.zdir)


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