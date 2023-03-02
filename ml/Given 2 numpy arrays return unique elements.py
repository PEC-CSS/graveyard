import numpy as np

array1 = np.array([1,2,3,4,5,6,7])
array2 = np.array([3,2,3,8,6,6,7])

if(array1.size==array2.size):
    arr = np.where(array1!=array2)
    arr_final = np.array([])
    for i in arr:
        arr_final = np.append(arr_final, [array1[i]])
    print(arr_final)
else:
    print("Not Comparable")