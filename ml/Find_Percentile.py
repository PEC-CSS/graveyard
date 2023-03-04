import numpy
m = int(input("Enter m"))
n = int(input("Enter n"))
p = int(input("Enter p"))
l = []
for a in range(m*n):
    x = int(input(f"Enter num {a+1}"))
    l.append(x)
arr = numpy.array(l)
arr = arr.reshape(m,n)
print(p,"th percentile of flattened array is ", numpy.percentile(arr,p),sep="")
print(p,"th percentile values of rows are ",numpy.percentile(arr,p,axis=0),sep="")
print(p,"th percentile values of columns are ",numpy.percentile(arr,p,axis=1),sep="")
