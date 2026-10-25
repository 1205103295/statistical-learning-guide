coef_ls, residual_sums, rank, singular_values = np.linalg.lstsq(
    X, y_multi, rcond=None
)
pred_multi = X @ coef_ls
res_multi = y_multi - pred_multi
rss_multi = np.sum(res_multi ** 2)
assert np.allclose(X.T @ res_multi, 0.0)
print("coefficients:", np.round(coef_ls, 6))
print("rank:", rank)
print("predictions:", np.round(pred_multi, 6))
print("residuals:", np.round(res_multi, 6))
print("RSS:", round(rss_multi, 6))
