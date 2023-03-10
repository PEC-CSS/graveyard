import os
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
sum=num1+num2
name_of_python_file=os.path.basename(__file__)
length_of_name=len(name_of_python_file)
name_of_python_file=name_of_python_file[0:length_of_name-3]+".txt"
f = open(name_of_python_file, "w")
f.write(str(sum))
f.close()