X_near = np.array([[1., 0., 0.], [1., 1., 1.],
                   [1., 2., 2.], [1., 3., 3.01]])
y_near = np.array([5., 6., 7., 8.])
y_changed = y_near.copy()
y_changed[-1] += 0.01
b_before = np.linalg.lstsq(X_near, y_near, rcond=None)[0]
b_after = np.linalg.lstsq(X_near, y_changed, rcond=None)[0]
sv = np.linalg.svd(X_near, compute_uv=False)
condition = sv[0] / sv[-1]
print("before:", np.round(b_before, 6))
print("after:", np.round(b_after, 6))
print("singular values:", np.round(sv, 6))
print("condition X:", round(condition, 3))
print("condition X.T X:", round(condition ** 2, 3))
