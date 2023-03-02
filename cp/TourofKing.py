
def TourofKing(T):
    lst = []
    for z in range(T):
        
        i=0
        x=input()
        n=""
        m=""
        
        while x[i]!=" ":
            n+=x[i]
            i+=1
        
        l = len(x)
        for k in range(i+1,l):
            m+=x[k]
            
        N = int(n)
        M = int(m)
        
        lst.append((N*5)+(M*7))
    
    for a in range(T):   
        print(lst[a])
        
T = int(input())
TourofKing(T)

    

