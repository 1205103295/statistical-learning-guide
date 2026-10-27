import numpy as np
x_knn = np.array([10., 20., 30., 40., 50.])
y_knn = np.array([4., 6., 8., 9., 11.])
query = 32.
distance = np.abs(x_knn - query)
neighbors = np.argsort(distance)[:3]
print('neighbor positions:', neighbors)
print('neighbor inputs:', x_knn[neighbors])
print('prediction:', y_knn[neighbors].mean())
