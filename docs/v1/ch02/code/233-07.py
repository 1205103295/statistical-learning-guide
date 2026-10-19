y_true = np.array([10.0, 12.0, 13.0])
residual = y_true - y_pred
mse = np.mean(residual ** 2)
print(residual)
print(mse)
assert y_true.shape == y_pred.shape
