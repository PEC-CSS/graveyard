lst = []
length = int(input("Number of samples : "))
for i in range(0,length):
  lst.extend(list(input("Enter digits : ")))
largest = "".join(sorted(lst))
print(largest[::-1])
