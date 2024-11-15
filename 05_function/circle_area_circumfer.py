import math
def area(rad):
    area =  math.pi * rad ** 2 
    circumfer = 2 * math.pi * rad
    return area, circumfer
a, c = area(3)

print(a,c)