y_fit = beta0_hat + beta1_hat * x
residual = y - y_fit
print("fitted values:", y_fit)
print("residuals:", residual)
print("residual shape:", residual.shape)
