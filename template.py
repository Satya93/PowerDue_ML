from regression import regression
import datasets as db
from kmeans import split
import time

data = db.randgen(100,0,100)

split(data,2)
#regression(data, 3.7, 0.00058)
print 

