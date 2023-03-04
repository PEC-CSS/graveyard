'''We will use sys.argv to get command line input.
For example if we type

py takeInputFromTerminal.py 1 2 6 1 4 8

in command line then sys.argv will give us a list consisting of
['takeInputFromTerminal.py', '1', '2', '6', '1', '4', '8']

We will use list slicing and comprehension to get the input and convert them into integers'''

import sys

list1 = [int(i) for i in sys.argv[1:]]

#Now we will define a function to find the maximum value.

def maximum(arr):
    #If no number is passed then we will give output 0
    if arr == []:
        return 0

    else:
        #Assume first element to be maximum
        current_max = arr[0]

        #Loop through the rest to check if there is an element greater than the current maximum.
        for j in arr[1:]:
            if j > current_max:
                current_max = j
        
        return current_max

print(maximum(list1))