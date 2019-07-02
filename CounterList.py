#6 Collections

import collections
from collections import Counter

#Containers
#list
#set
#dict
#tuple - inmutable

#Types
#1. counter
#2.deque
#3. nameTupled
#4. orderDict
#5. defaultDict


c = Counter('gallad')
print(c)
c = Counter(['a','b','c','c','d'])
print(c)
c = Counter({'a':1,'b':2})
print(c)
c = Counter(cats=4,dogs=5)
print(c['pets'])

print(list(c.elements()))

print(c.most_common(3))

c = Counter(a=2,b=1,c=0,d=5)

d = ['a','a','b','d','d','d']

c.subtract(d)

print(c)

c.update(d)

print(c)

c.clear()

print(c)



t = Counter(a=1,b=2,c=1)
e = Counter(['a','b','c'])

print(t+e)
print(t-e)