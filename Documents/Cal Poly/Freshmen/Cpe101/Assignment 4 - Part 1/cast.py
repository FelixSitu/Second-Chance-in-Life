from Data import *
from vector_math import *
#import pygame
import sys
import math
from utility import *
from fold import *
from collisions import *

"""def discriminant(a,b,c):
    return b**2 - 4*a*c

def quadratic_formula(a,b,c):
    t1 = (-b + math.sqrt(discriminant(a,b,c)))/(2*a)
    t2 = (-b - math.sqrt(discriminant(a,b,c)))/(2*a)
    return [t1,t2]

def compute_coefficient(theSphere,theRay):
    A = dot_vector(theRay.dir,theRay.dir)
    vector_from_center_to_raypt = vector_from_to(theSphere.center,theRay.pt)
    #B = dot_vector(scale_vector(difference_point(theRay.pt,theSphere.center),2),theRay.dir)
    B = dot_vector(scale_vector(vector_from_center_to_raypt,2),theRay.dir)
    C = dot_vector(difference_point(theRay.pt,theSphere.center),difference_point(theRay.pt,theSphere.center)) - theSphere.radius**2
    return A,B,C

def sphere_intersection_point(ray,sphere):
    # find coefficients
    a,b,c = compute_coefficient(sphere,ray)
    dis = discriminant(a,b,c)
    if  dis < 0: #test for no intersections
        return None
    else: #tests for real roots
        t1,t2 = quadratic_formula(a,b,c)
        if t1 < 0 and t2 < 0:
            return None
        else:
            lst = [t1,t2]
            idx = index_of_smallest(lst)
            t = lst[idx]
            pt = translate_point(ray.pt, scale_vector(ray.dir, t))
            return pt

def find_intersection_points(sphere_list,ray):
    lst = []
    for sphere in sphere_list:
        ipt = sphere_intersection_point(ray,sphere)
        if ipt != None:
            point_sphere_lst = [sphere,ipt]
            lst.append(point_sphere_lst)
    return lst"""



def cast_ray(ray,sphere_list):
    intersection = find_intersection_points(sphere_list,ray)
    if len(intersection) > 0:
        return True
    else:
        return False

def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list):
    #pygame.init()
    #screen = pygame.display.set_mode((width,height))
    delta_x = (max_x - min_x) / float(width)
    delta_y = (max_y - min_y) / float(height)
    h = 0
    y = max_y
    while h < height:
        w = 0
        x = min_x
        while w < width: #takes every single x,y component
            rayDir = vector_from_to(eye_point,Point(x,y,0))
            ray = Ray(eye_point,rayDir)
            #print rayDir
            #print ray
            if cast_ray(ray, sphere_list) == True: #Print Black
                print 0, 0, 0
                #screen.set_at((w,h),(0,0,0))
            else:
                #screen.set_at( (w, h), (255, 255, 255) ) #Print White
                print 255, 255, 255


            #pygame.display.update()

            x += delta_x
            w += 1

        y -= delta_y
        h += 1
