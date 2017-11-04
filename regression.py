from matplotlib import pyplot as plt
import time

def regression(data,lim,alp):
    plt.ion()
    
    slp = 10
    intercept = sum(data)/len(data)
    axis = range(0,len(data))
    alpha = alp
    numel = len(data) 
    x = 0
    toterr_0 = 0
    toterr_1 = 0
    totcost = 10000

    while totcost > lim:
        targ_array = []
        x = 0
        v = 0
        u = 0
        toterr_0 = 0
        toterr_1 = 0
        totcost = 0
        while x < numel:
            targ_val = slp*(x+1)+intercept
            targ_array.append(targ_val)
            err_0 = (targ_val-data[x])
            err_1 = (targ_val-data[x])*x
            toterr_0 += err_0
            toterr_1 += err_1
            cost = (targ_val-data[x])*(targ_val-data[x])
            sv = data[x] - sum(data)/len(data)
            v+=sv
            totcost += cost
            x = x+1
        u = totcost
        score = 1-(u/v)
        totcost = totcost/(2*numel)
        #print "At slope = ", slp, " and intercept = ", intercept, " Total cost is : ", totcost
        print "Score = ", score, " Total cost is : ", totcost
        #print totcost
        delta_0 = alpha*toterr_0/numel
        delta_1 = alpha*toterr_1/numel
        intercept = intercept-delta_0
        slp = slp-delta_1
    for p in range(1, numel+1):
        val = slp*p+intercept
        print val
    return slp*(numel+1)+intercept