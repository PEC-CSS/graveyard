no_of_testcases=int(input())
list_of_integers1=[]
list_of_integers2=[]
for i in range(no_of_testcases):
    a, b=map(int, input().split())
    list_of_integers1.append(a)
    list_of_integers2.append(b)
for i in range(no_of_testcases):
    floor=list_of_integers1[i]//list_of_integers2[i]
    if(list_of_integers1[i]%list_of_integers2[i]==0):
        ceil=floor
    else:
        ceil=floor+1
    print(floor,ceil)