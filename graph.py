from matplotlib import pyplot as plt

d1 = [47,77,86,46,58,76,41,70,71,55]
d2 =[]
m = -0.25
c = 64
i = 0
while(i<len(d1)):
    d2.append(m*(i+1)+c)
    i+=1

print d2
plt.plot(d2,d1,"-",d2,d2,"-.")
plt.show()