import numpy as np
x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 3.0, 5.0])
dx = x - x.mean()
dy = y - y.mean()
sxx = np.sum(dx ** 2)
sxy = np.sum(dx * dy)
slope = sxy / sxx
intercept = y.mean() - slope * x.mean()
y_pred = intercept + slope * x
print("intercept, slope:", np.round([intercept, slope], 6))
print("predictions:", np.round(y_pred, 6))
