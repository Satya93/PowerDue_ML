from regression import regression
from kmeans import split
import time
import random

data = []
ele = 0
while ele < 100:
    data.append(random.randint(20,50))
    ele+=1


print data
print 

regression(data,0.02,0.0005)
#split(data,2)
print 

