import numpy as np
# importing NumPy
arr = np.arange(20).reshape(5,4)
#original array
array1 = arr[:, :1]#array 1
array2 = arr[:, 1:]#array 2
#printing results
print("Array1")
print(array1.tolist())
print("\nArray2")
for row in array2:
    if row[0] in [1, 5]:
        print(row.tolist())
    else:
        print(row.tolist())