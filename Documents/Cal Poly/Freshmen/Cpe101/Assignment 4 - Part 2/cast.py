from Data import *
from vector_math import *
import pygame
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
    distance1 = distance(ray.pt,intersection[0][1])
    distance2 = distance(ray.pt,intersection[1][1])
    if len(intersection) != None:
        if distance1 < distance2:
            return sphere_list[0].color.r,sphere_list[0].color.g,sphere_list[0].color.b
        else:
            return sphere_list[1].color.r,sphere_list[1].color.g,sphere_list[1].color.b

"""def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list):
    pygame.init()
    screen = pygame.display.set_mode((width,height))
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
            intersection = find_intersection_points(sphere_list, ray)
            if len(intersection) > 1 and cast_ray(ray,sphere_list) == (255,0,0):
                print sphere_list[0].color.r,sphere_list[0].color.g,sphere_list[0].color.b
                screen.set_at((w,h),(sphere_list[0].color.r,sphere_list[0].color.g,sphere_list[0].color.b))
            else:
                screen.set_at( (w, h), (255, 255, 255) ) #Print White
                print 255, 255, 255
            x += delta_x
            w += 1

        y -= delta_y
        h += 1
        pygame.display.update()"""

'''def cast_ray(ray,sphere_list):
    intersection = find_intersection_points(sphere_list,ray)
    for sphereIdx in range(0,len(sphere_list),1):
        if intersection != None:
            return sphere_list[sphereIdx]
        else:
            return None'''

"""def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    delta_x = (max_x - min_x) / float(width)
    delta_y = (max_y - min_y) / float(height)
    h = 0
    y = max_y
    while h < height:
        w = 0
        x = min_x
        while w < width:  # takes every single x,y component
            rayDir = vector_from_to(eye_point, Point(x, y, 0))
            ray = Ray(eye_point, rayDir)
            intersection = find_intersection_points(sphere_list,ray)
            if len(intersection) > 1:
                if cast_ray(ray, sphere_list) == sphere_list[0]:
                    sphere1 = sphere_list[0]
                    print sphere1.color.r, sphere1.color.g, sphere1.color.b
                    screen.set_at((w, h), (sphere1.color.r, sphere1.color.g, sphere.color1.b))
                    sphere2 = sphere_list[1]
                    print sphere2.color.r, sphere2.color.g, sphere2.color.b
                    screen.set_at((w, h), (sphere2.color.r, sphere2.color.g, sphere.color2.b))
                elif cast_ray(ray, sphere_list) == sphere_list[1]:
                    sphere2 = sphere_list[1]
                    print sphere2.color.r, sphere2.color.g, sphere2.color.b
                    screen.set_at((w, h), (sphere2.color.r, sphere2.color.g, sphere.color2.b))
                    sphere1 = sphere_list[0]
                    print sphere1.color.r, sphere1.color.g, sphere1.color.b
                    screen.set_at((w, h), (sphere1.color.r, sphere1.color.g, sphere.color1.b))
                else:
                    screen.set_at((w, h), (255, 255, 255))  # Print White
                    print 255, 255, 255
            else:
                screen.set_at((w, h), (255, 255, 255))  # Print White
                print 255, 255, 255

            x += delta_x
            w += 1

        y -= delta_y
        h += 1
        pygame.display.update()
"""

def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    delta_x = (max_x - min_x) / float(width)
    delta_y = (max_y - min_y) / float(height)
    h = 0
    y = max_y
    while h < height:
        w = 0
        x = min_x
        while w < width:  # takes every single x,y component
            rayDir = vector_from_to(eye_point, Point(x, y, 0))
            ray = Ray(eye_point, rayDir)
            sphere1 = sphere_list[0]
            sphere2 = sphere_list[1]
            intersection = find_intersection_points(sphere_list, ray)
            if len(intersection) > 1: #If the ray crosses both two spheres: Find two intersection point
                if cast_ray(ray, sphere_list) == (sphere_list[0].color.r,sphere_list[0].color.g,sphere_list[0].color.b):
                    print sphere1.color.r*255, sphere1.color.g*255, sphere1.color.b*255
                    screen.set_at((w, h), (sphere1.color.r*255, sphere1.color.g*255, sphere1.color.b*255))
                elif cast_ray(ray, sphere_list) == (sphere_list[1].color.r,sphere_list[1].color.g,sphere_list[1].color.b):
                    print sphere2.color.r*255, sphere2.color.g*255, sphere2.color.b*255
                    screen.set_at((w, h), (sphere2.color.r*255, sphere2.color.g*255, sphere2.color.b*255))
            elif len(intersection) > 0: #If the ray crosses only one spheres: Find one intersection point
                if sphere2.radius > sphere1.radius:
                    print sphere2.color.r*255, sphere2.color.g*255, sphere2.color.b*255
                    screen.set_at((w, h), (sphere2.color.r*255, sphere2.color.g*255, sphere2.color.b*255))
                else:
                    print sphere1.color.r*255, sphere1.color.g*255, sphere1.color.b*255
                    screen.set_at((w, h), (sphere1.color.r*255, sphere1.color.g*255, sphere1.color.b*255))
            else: #If the ray crosses NO spheres
                print 255, 255, 255
                screen.set_at((w, h), (255, 255, 255))  # Print White


            x += delta_x
            w += 1

        y -= delta_y
        h += 1

        pygame.display.update()

"""def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    delta_x = (max_x - min_x) / float(width)
    delta_y = (max_y - min_y) / float(height)
    h = 0
    y = max_y
    while h < height:
        w = 0
        x = min_x
        while w < width:  # takes every single x,y component
            rayDir = vector_from_to(eye_point, Point(x, y, 0))
            ray = Ray(eye_point, rayDir)
            intersection = find_intersection_points(sphere_list, ray)
            if cast_ray(ray, sphere_list) != None and len(intersection) > 1:
                for sphere in sphere_list:
                    print 255,0,0
                    screen.set_at((w, h), (255,0,0))
            elif cast_ray(ray, sphere_list) != None and len(intersection) > 0:
                for sphere in sphere_list:
                    print 0,0,255
                    screen.set_at((w, h), (0,0,255))
            else:
                print 255, 255, 255
                screen.set_at((w, h), (255, 255, 255))  # Print White


            x += delta_x
            w += 1

        y -= delta_y
        h += 1

        pygame.display.update()"""

