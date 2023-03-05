import matplotlib.pyplot as plt
import numpy as np

# Input data
ageA = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
speedA = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
ageB = [2, 2, 8, 1, 15, 8, 12, 9, 7, 3, 11, 4, 7, 14, 12]
speedB = [100, 105, 84, 105, 90, 99, 90, 95, 94, 100, 79, 112, 91, 80, 85]

# Plotting the data
plt.scatter(ageA, speedA, color='b', label='Manufacturer A')
plt.scatter(ageB, speedB, color='y', label='Manufacturer B')

# Set axis labels and title
plt.xlabel('Age (years)')
plt.ylabel('Speed (km/h)')
plt.title('Car Manufacturers A and B')

# Set legend and grid
plt.legend()
plt.grid()

# Display the plot
plt.show()