import string
import sys #import system


def float_default(string):
    try:
        line = float(string)
        return line
    except:
        return string
