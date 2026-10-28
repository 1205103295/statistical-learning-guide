weights = p * (1.0 - p)
weighted_X = weights[:, None] * X
H = X.T @ weighted_X / n
print('weights:', weights)
print('weighted X:')
print(weighted_X)
print('Hessian:')
print(np.round(H, 6))
