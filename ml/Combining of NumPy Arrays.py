import numpy as np

arr1 = np.array([1,2,3,4,5,6,7,8])
arr2 = np.array([[1,2,3,4], [10,9,8,7]])

n1 = arr1.size
n2 = arr2.size

if(n1==n2):
    v_stack = np.vstack((arr1.reshape(1, n1), arr2.reshape(1, n1)))
    h_stack = np.hstack((arr1.reshape(n1, 1), arr2.reshape(n1, 1)))

    print(f"Vertical stacking\n{v_stack}\n\nHorizontal stacking\n{h_stack}")
else:
    print("Arrays cannot be stacked")