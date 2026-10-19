beta = np.array([0.04, 0.10])
contributions = X * beta
print(contributions)
print(X @ beta)
intercept = 5.0
y_pred = intercept + X @ beta
print(y_pred)
print(y_pred.shape)
