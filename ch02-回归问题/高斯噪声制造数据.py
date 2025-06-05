import numpy as np

data = []
for i in range(100):
	x = np.random.uniform(3., 12.)
	# mean=0, std=0.1
	eps = np.random.normal(0., 0.1)
	y = 1.477 * x + 0.089 + eps
	data.append([x, y])
data = np.array(data)
print(data.shape, data)