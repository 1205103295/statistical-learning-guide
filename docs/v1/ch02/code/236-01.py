y = np.array([11.0, 12.0, 11.2, 13.8])
mask = X[:, 0] >= 100
X_selected = X[mask, :]
y_selected = y[mask]
print(mask)
print(X_selected)
print(y_selected)
print(X_selected.shape, y_selected.shape)
