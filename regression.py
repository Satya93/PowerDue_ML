import time

def regression(data,lim, alp):
    slp = 2
    intercept = sum(data)/len(data)
    alpha = alp
    numel = len(data)
    x = 0
    toterr_0 = 0
    toterr_1 = 0
    totcost = 10000

    while totcost > lim:
        x = 0
        toterr_0 = 0
        toterr_1 = 0
        totcost = 0
        while x < numel:
            targ_val = slp*(x+1)+intercept
            err_0 = (targ_val-data[x])
            err_1 = (targ_val-data[x])*x
            toterr_0 += err_0
            toterr_1 += err_1
            cost = (targ_val-data[x])*(targ_val-data[x])
            totcost += cost
            x = x+1
        totcost = totcost/(2*numel)
        print "At slope = ","%.2f" % slp, " and intercept = ", "%.2f" % intercept, " Total cost is : ", totcost
        #print totcost
        delta_0 = alpha*toterr_0/numel
        delta_1 = alpha*toterr_1/numel
        intercept = intercept-delta_0
        slp = slp-delta_1
        #time.sleep(1)

    for p in range(1, numel+1):
        val = slp*p+intercept
        print val
    return [slp,intercept]