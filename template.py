from regression import regression
from kmeans import split
import time
import random

data = []
ele = 0
while ele < 10:
    data.append(random.randint(20,50))
    ele+=1

print data
print 

split(data,2)

