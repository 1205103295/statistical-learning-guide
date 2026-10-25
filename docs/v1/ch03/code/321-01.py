features = np.array([[10., 5.], [20., 10.],
                     [30., 5.], [40., 15.]])
y_multi = np.array([6., 8., 7., 9.])
n = len(y_multi)
X = np.column_stack((np.ones(n), features))
print("features, X, y:", features.shape, X.shape, y_multi.shape)
print(X)
