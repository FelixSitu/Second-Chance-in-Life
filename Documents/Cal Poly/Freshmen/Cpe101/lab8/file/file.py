from string import *
from sys import *


filename = argv[1]
try:
    f = open(filename)
except:
    exit()

for line in f:
    values = split(line)
    try:
        sum = float(values[0]) + float(values[1])
        print sum
    except:
        print "Error"
f.close()
