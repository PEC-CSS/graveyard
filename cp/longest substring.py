s=str(input())
k=int(input())
d={}
length=0
if (1 <= len(s) <= 10**4) and (1 <= k <= 26):
    for p in range(len(s)):
        d[s[p]]=s.count(s[p])

    sorted_d = sorted(d.items(), key=lambda x:x[1], reverse=True)

    for i in range(k):
        length=length+sorted_d[i][1]
    print(length)
