
n = int(input())
a = 0
b = 1
c = 2
sum=0

if (n >= 2):
    print(0, end=" ")
    while (c < n+1):
        temp = b
        b += a
        a = temp
        print(a, end=" ")
        c+=1
        sum+=a
        
    avg = sum/n
    print("\n",avg)

else:
    print(0)
    print(0)
        
