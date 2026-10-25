x_curve = np.arange(5, dtype=float)
y_curve = 2 + x_curve ** 2
X_line = np.column_stack((np.ones(5), x_curve))
X_quad = np.column_stack((np.ones(5), x_curve, x_curve ** 2))
b_line = np.linalg.lstsq(X_line, y_curve, rcond=None)[0]
b_quad = np.linalg.lstsq(X_quad, y_curve, rcond=None)[0]
e_line = y_curve - X_line @ b_line
e_quad = y_curve - X_quad @ b_quad
print("line coefficients:", np.round(b_line, 6))
print("quadratic coefficients:", np.round(b_quad, 6))
print("line residuals:", np.round(e_line, 6))
print("quadratic RSS:", round(np.sum(e_quad ** 2), 6))
