residual = y - y_pred
rss = np.sum(residual ** 2)
tss = np.sum(dy ** 2)
ess = np.sum((y_pred - y.mean()) ** 2)
r = sxy / np.sqrt(sxx * tss)
r2 = 1 - rss / tss
assert np.isclose(tss, ess + rss)
assert np.isclose(r2, r ** 2)
print("RSS, TSS, ESS:", np.round([rss, tss, ess], 6))
print("r, R2:", np.round([r, r2], 6))
