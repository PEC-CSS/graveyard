import numpy as np

berlin_vec = np.array([-0.562, 0.630, -0.453, -0.299, -0.006])
germany_vec = np.array([0.194, 0.507, 0.287, 0.132, -0.281])
france_vec = np.array([0.605, -0.678, -0.436, -0.019, -0.291])
paris_vec = np.array([-0.074, -0.855, -0.689, -0.057, -0.139])

result_vec = berlin_vec - germany_vec + france_vec
print(result_vec)

diff_vec = result_vec - paris_vec

print(diff_vec)
