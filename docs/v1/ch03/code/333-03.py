x_influence = np.array([1., 2., 3., 4., 5., 20.])
y_influence = np.array([5., 8., 11., 14., 17., 40.])
Xi = np.column_stack((np.ones(6), x_influence))
bi = np.linalg.lstsq(Xi, y_influence, rcond=None)[0]
Hi = Xi @ np.linalg.pinv(Xi)
leverage = np.diag(Hi)
bi_without = np.linalg.lstsq(Xi[:-1], y_influence[:-1], rcond=None)[0]
print("leverage:", np.round(leverage, 6))
print("full coefficients:", np.round(bi, 6))
print("without last point:", np.round(bi_without, 6))
print("last residual:", round((y_influence - Xi @ bi)[-1], 6))
