import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

meanColumn = arr.mean(axis=0)

print(meanColumn)