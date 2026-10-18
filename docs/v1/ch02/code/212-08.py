import matplotlib.pyplot as plt
from pathlib import Path

X_grid = np.linspace(10.0, 50.0, 201).reshape(-1, 1)
linear_curve = linear_model.predict(X_grid)
knn_curve = knn_model.predict(X_grid)
