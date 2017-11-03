from regression import regression
from kmeans import split
from matplotlib import pyplot as plt
import time
import random

data = []
data_length = 100
ele = 0
while ele < data_length:
    data.append(random.randint(20,50))
    ele+=1


print data
print 

reg_arr = regression(data,40,0.00055)
#split(data,2)
axis = range(0,data_length)
fit = [reg_arr[0]*x + reg_arr[1] for x in axis]
plt.plot(axis,data,"-",axis,fit,"-")
plt.show()
print 

