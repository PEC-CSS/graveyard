import numpy as np
arr1 =np.array([])
s=(int)(input("enter size of the array:"))
for i in range (s):
    a=(int)(input("enter element:"))
    arr1=np.append(arr1,a)
arr2 =np.array([])
l=(int)(input("enter the beginning no.:"))
r=(int)(input("enter the ending no.:"))
for j in arr1:
    if (j>=l and j<=r):
        arr2=np.append(arr2,j)
print(arr2)