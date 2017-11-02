def split(data, cat):
    numcat = cat
    numel = len(data)
    gr = []
    cnt = 1
    while cnt < numcat+1:
        label = "Category "+str(cnt)
        label = [label]
        gr.append(label)
        cnt+=1

    dist_local = []
    dist = []
    while cnt < numel:
        cnt2 = 0
        dist_local = []
        while cnt2 < numel:
            dist_local.append(abs(data[cnt] - data[cnt2]))
            cnt2+=1
        #print dist_local
        dist.append(dist_local)
        cnt+=1

    maxes = max(data)
    mins = min(data)
    print "Minimum value : ",mins
    print "Maximum value : ",maxes
    dist_from_largest = dist[data.index(maxes)]
    #print dist_from_largest
    #print max(dist_from_largest)
    print 

    cat_cnt = 1
    cat_thresh = []
    while cat_cnt<numcat:
        #print cat_cnt
        cat_thresh.append((cat_cnt*(max(dist_from_largest)/numcat)))
        #print cat_thresh
        #print 
        cat_cnt+=1
    print "Threshold is : ", cat_thresh[0]
    print 

    cat_cnt = 0
    dat_cnt = 0
    while dat_cnt<numel:
        if dist_from_largest[dat_cnt] > cat_thresh[0]:
            gr[0].append(data[dat_cnt])
        if dist_from_largest[dat_cnt] < cat_thresh[0]:
            gr[1].append(data[dat_cnt])
        dat_cnt+=1
    print gr[0]
    print gr[1]
    #print data.index(maxes)
    #print data.index(mins)