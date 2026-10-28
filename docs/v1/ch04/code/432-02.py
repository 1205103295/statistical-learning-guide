eta = X @ beta
p = 1.0 / (1.0 + np.exp(-eta))
grad = X.T @ (p - y) / n
print('eta:', eta)
print('p:', p)
print('gradient:', np.round(grad, 6))
