def X (sspace):
    for n in range(0,len(sspace)):
        if (sspace[n].count('H')==2):
            print(-1)
        else:
            print(1)
sspace=('HH','HT','TH','TT')
X(sspace)

    

