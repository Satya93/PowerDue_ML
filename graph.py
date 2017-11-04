from matplotlib import pyplot as plt
from datasets import linear_with_disturbance as ld

d1 = ld()
d2 =[]
d3 = []
m = 1.001
c = 5.26
m2 = 0.98
c2 = 6.02
i = 0
axis = range(0,100)
while(i<len(d1)):
    d2.append(m*(i+1)+c)
    d3.append(m2*(i+1)+c2)
    i+=1

print d2
plt.plot(axis,d1,".",axis,d2,"-",axis,d3,"-.")
plt.show()