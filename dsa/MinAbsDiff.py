
def MinAbsDiff(arr):
    d=1000000
    arr.sort()
    l = len(arr)
    lst = []

    for i in range(l-1):
        x=arr[i+1]-arr[i]
        if x<d:
            d=x
    for i in range(l-1):
        if arr[i+1]-arr[i] == d:
            lst.append([arr[i],arr[i+1]])
            
    print(lst)
    return lst

arr=eval(input())
MinAbsDiff(arr)