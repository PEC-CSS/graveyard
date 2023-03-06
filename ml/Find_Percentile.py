import numpy
m = int(input("Enter m"))
n = int(input("Enter n"))
p = int(input("Enter p"))
arr = numpy.zeros((m,n),dtype=int)
for a in range(m):
    for b in range(n):
        arr[a][b]= int(input(f"Enter num"))
print(arr)
print(p,"th percentile of flattened array is ", numpy.percentile(arr,p),sep="")
print(p,"th percentile values of rows are ",numpy.percentile(arr,p,axis=0),sep="")
print(p,"th percentile values of columns are ",numpy.percentile(arr,p,axis=1),sep="")
