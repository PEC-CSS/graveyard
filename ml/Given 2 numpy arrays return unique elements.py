import numpy as np

array1 = np.array([1,2,3,4,5,6,7])
array2 = np.array([3,2,3,8,6,6,7])

if(array1.size==array2.size):
    print(np.unique(array1[np.where(array1!=array2)]))
else:
    print("Not Comparable")
