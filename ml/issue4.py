import numpy as np
arrayOne = np.array([1,2,3,2,3,4,3,4,5,6])
arrayTwo = np.array([7,2,10,2,7,4,9,4,9,8])
match_positions = np.where(arrayOne == arrayTwo)[0]
print("Match positions: ", match_positions)
concatenated_array = np.concatenate((arrayOne, arrayTwo))
print("Concatenated array: ", concatenated_array)
