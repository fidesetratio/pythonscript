import collections
from collections import namedtuple

Point = namedtuple('Point',{'x':1,'y':2,'k':0})


newPoint = Point(1,2,3)
print(newPoint)

print(newPoint.x,newPoint.y, newPoint.k)
print(newPoint._fields)

newPoint = newPoint._replace(x=7)
print(newPoint)

p2 = Point._make(['a','b','c'])

print(p2)