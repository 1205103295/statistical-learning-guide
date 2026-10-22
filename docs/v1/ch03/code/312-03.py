sigma2_hat = rss / residual_df
rse = np.sqrt(sigma2_hat)
slope_se = rse / np.sqrt(Sxx)
print("estimated noise variance:", sigma2_hat)
print("RSE:", rse)
print("estimated slope SE:", slope_se)
