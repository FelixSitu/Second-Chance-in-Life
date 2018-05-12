import unittest
from vector_math import *
from cast import *
from collisions import *

width = 512
height = 384
eyepoint = Point(0.0,0.0,-14.0)
sphere1 = Sphere(Point(0.5,1.5,-3.0),0.5) #Small Sphere
sphere2 = Sphere(Point(1.0,1.0,0.0),2) #Big Sphere
sphereLst = [sphere1,sphere2]
print 'P3'
print  width, height
print '255'
cast_all_rays(-10,10,-7.5,7.5,512,384,eyepoint,sphereLst)

if __name__ == '__main__':
    unittest.main()
