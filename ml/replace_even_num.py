import numpy
arr = numpy.array([4, 1, 5, 2, 9, 10, 12, 19])
mean = numpy.mean(arr)
arr[arr%2==0]=mean
print(arr)
