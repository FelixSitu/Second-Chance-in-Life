import math

def max_101(x1,x2):
    if x1 > x2:
        return x1
    elif x2 > x1:
        return x2

def max_of_three(x1,x2,x3):
    """xp1 = max_101(x1, x2)
    xp2 = max_101(x3, xp1)"""
    if x1 > x2 and x1 > x3:
        return x1
    elif x2 > x1 and x2 > x3:
        return x2
    elif x3 > x1 and x3 > x2:
        return x3

def rental_late_fee(days):
    dollars = 0
    if days <= 0:
        dollars = 0
    if 0 > days <= 9:
        dollars = 5
    if 9 > days <= 15:
        dollars = 7
    if 15 < days <= 24:
        dollars = 19
    if days > 24:
        dollars = 100
    return dollars
