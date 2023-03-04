str=input()
d={}
output=""
for i in str:
    d[i]=1
for i in str:
    if d[i]==1:
        output=output+i
    d[i]=0

print(output)