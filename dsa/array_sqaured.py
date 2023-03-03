def square(arr):

    n=len(arr)

    ele = 0
    for ele in range(n):
        if arr[ele]>=0:
            break
#The value of i will be the index of first positive number

    i=ele-1  #Index for left(-ve) side
    j=ele     #Index for right(+ve) side
    k=0     #Index for merged array

    list=[0]*n

    while ((i>=0) and (j<n)):
        if (arr[i]*arr[i])<(arr[j]*arr[j]):
            list[k]=arr[i]*arr[i]
            i=i-1
            k=k+1
        else:
            list[k]=arr[j]*arr[j]
            j=j+1
            k=k+1
    while (i >= 0):
         
        list[k] = arr[i] * arr[i]
        i = i- 1
        k = k+ 1
         
    while (j < n):
        list[k] = arr[j] * arr[j]
        j = j+ 1
        k = k+ 1

    return list

arr=input("Enter elements of the input list separated by commmas:").split(",")
for q in range(len(arr)):
    arr[q]=int(arr[q])

print(square(arr))