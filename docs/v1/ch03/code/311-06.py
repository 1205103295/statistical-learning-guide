squared_residual = residual ** 2
rss = np.sum(squared_residual)
train_mse = np.mean(squared_residual)
print("squared residuals:", squared_residual)
print("RSS:", rss)
print("training MSE:", train_mse)
print("square of residual sum:", residual.sum() ** 2)
