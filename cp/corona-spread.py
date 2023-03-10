T = int(input())
for cases in range(0,T):
    N = int(input())
    Xi = [int(xi) for xi in input().split()]
    
    Xi.sort()
    
    t = 0
    m = Xi[-1]
    f = Xi.index(m)
    emptylist = []
    
    count = 1
    worstcase = 0
    bestcase = 100
    
    for i in Xi:
        if t+1 <= f:
            nextel = Xi[t+1]
            
            t += 1
            diff = nextel - i
            emptylist.append(diff)
    )
    for y in emptylist:
        if y <=2:
            count += 1
            
        else:
            if count > worstcase:
                worstcase = count
            if count < bestcase:
                bestcase = count
            count = 1
    if count > worstcase:
        worstcase = count
    if count < bestcase:
        bestcase = count

    print(bestcase,worstcase)
            
            

         
            
        
        
    