H = X @ C @ X.T
M = np.eye(n) - H
assert np.allclose(H @ H, H)
assert np.allclose(M @ X, 0.0)
assert np.allclose(M @ y_multi, res_multi)
print("trace H, trace M:", np.round([np.trace(H), np.trace(M)], 6))
print("RSS from projection:", round(y_multi @ M @ y_multi, 6))
