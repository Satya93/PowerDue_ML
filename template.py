from regression import regression
from datasets import linear_with_disturbance as ld
from kmeans import split
import time
import random

data = ld()

split(data,2)
#regression(data, 3.7, 0.00058)
print 

