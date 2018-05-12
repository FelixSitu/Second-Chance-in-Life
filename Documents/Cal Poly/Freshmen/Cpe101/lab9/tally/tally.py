from string import *
from sys import *


filename = argv[1] #the input txt
column_num = int(argv[2])

try:
    f = open(filename)
except:
    print "filename does not exist"
    exit()

values = 0

for line in f:
    valueLst = split(line)
    try:
        values += float(valueLst[column_num])
    except ValueError:
        print "Not a Number"
    except IndexError:
        print "Out of Range"
print values



