from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

X = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
X = X.reshape(len(X), 1)
Y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])

model = LinearRegression()

model.fit(X, Y)

slope = model.coef_[0]
intercept = model.intercept_

print("Slope:", slope)
print("Intercept:", intercept)

plt.scatter(X, Y, color='m')
plt.plot(X, slope*X + intercept, color='g')
plt.ylabel("Y-axis")
plt.xlabel("X-axis")
plt.show()
