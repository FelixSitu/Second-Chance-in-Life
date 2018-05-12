import math
from vector_math import *
from utility import *
from fold import *

def discriminant(a,b,c):
    return b**2 - 4*a*c

def quadratic_formula(a,b,c):
    t1 = (-b + math.sqrt(discriminant(a,b,c)))/(2*a)
    t2 = (-b - math.sqrt(discriminant(a,b,c)))/(2*a)
    return [t1,t2]

def compute_coefficient(theSphere,theRay):
    A = dot_vector(theRay.dir,theRay.dir)
    vector_from_center_to_raypt = difference_point(theRay.pt,theSphere.center)
    #B = dot_vector(scale_vector(difference_point(theRay.pt,theSphere.center),2),theRay.dir)
    B = dot_vector(vector_from_center_to_raypt,theRay.dir) * 2
    C = dot_vector(vector_from_center_to_raypt,vector_from_center_to_raypt) - theSphere.radius**2
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
        elif t1 < 0:
            return translate_point(ray.pt, scale_vector(ray.dir,t2))
        elif t2 <0:
            return translate_point(ray.pt, scale_vector(ray.dir,t1))
        else:
            lst = [t1,t2]
            idx = index_of_smallest(lst)
            t = lst[idx]
            pt = translate_point(ray.pt, scale_vector(ray.dir, t))
            return pt

def find_intersection_points(sphere_list,ray):
    lst1 = sphere_list
    lst = []
    for sphere in lst1:
        ipt = sphere_intersection_point(ray,sphere)
        if ipt != None:
            point_sphere_lst = (sphere,ipt)
            lst.append(point_sphere_lst)
    return lst


def sphere_normal_at_point(sphere,point):
    norm_vec = difference_point(sphere.center,point)
    return normalize_vector(norm_vec)


