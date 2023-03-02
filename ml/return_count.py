import numpy
def count(arr,num):
    count = numpy.count_nonzero(arr==num)
    return count
l = eval(input("Enter list of data"))
arr = numpy.array(l)
num=int(input("Enter a number to be counted"))
cnt = count(arr,num)
print(cnt)