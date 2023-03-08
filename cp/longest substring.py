s=str(input())
k=int(input())
output=[]
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        set1=set(s[i:j])
        if len(set1)<=k:
            output.append((j-i))
print(max(output))
