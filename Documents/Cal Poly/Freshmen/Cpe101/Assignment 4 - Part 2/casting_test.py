import unittest
from vector_math import *
from cast import *
from collisions import *
from Data import *


eyepoint = Point(0.0,0.0,-14.0)
red = Color(1,0,0)
blue = Color(0,0,1)
sphere1 = Sphere(Point(1.0,1.0,0.0),2,red) #Small Sphere
sphere2 = Sphere(Point(1.0,1.0,-2.0),.5,blue) #Big Sphere
sphereLst = [sphere1,sphere2]
print 'P3'
print '512 384'
print '255'
cast_all_rays(-10,10,-7.5,7.5,512,384,eyepoint,sphereLst)

if __name__ == '__main__':
    unittest.main()
