y_test_array = y_test.to_numpy()
errors = y_test_array - baseline_pred
baseline_test_mse = np.mean(errors ** 2)
print(errors)
print(baseline_test_mse)
