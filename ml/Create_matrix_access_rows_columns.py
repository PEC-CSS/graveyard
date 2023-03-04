import numpy
arr = numpy.arange(10,50,2)
arr = arr.reshape(4,5)
print("Created array is :")
print(arr,'\n')
print("Third column is :",arr.T[2],'\n')
arr2 = numpy.arange(1,6)
arr[3] = arr2
print("Array after changing fourth row is :")
print(arr)
