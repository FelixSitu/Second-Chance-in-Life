import math
# need to make polynomial: 2.7x**2 + 3.1x + 2
poly = [2,3.1,2.7]

def poly_add2(lst1,lst2):
    return [lst1[0] + lst2[0], lst1[1] + lst2[1] , lst1[2] + lst2[2]]

def poly_mult2(lst1,lst2):
    polynomial = [0,0,0,0,0]
    polynomial[0] = lst1[0] + lst2[0]
    polynomial[1] = lst1[0]*lst2[1] + lst1[1]*lst2[0]
    polynomial[2] = lst1[2]*lst2[0] + lst1[1]*lst2[1] + lst1[0]*lst2[2]
    polynomial[3] = lst1[2]*lst2[1] + lst1[1]*lst2[2]
    polynomial[4] = lst1[2] + lst2[2]
    return [polynomial[4],polynomial[3],polynomial[2],polynomial[1],polynomial[0]]
