n = len(y)
residual_df = n - 2
rss = np.sum(residual ** 2)
print("n:", n)
print("residual degrees of freedom:", residual_df)
print("RSS:", rss)
