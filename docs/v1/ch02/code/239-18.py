final_errors = y_test.to_numpy() - final_pred
final_mse = np.mean(final_errors ** 2)
results = pd.DataFrame({
    "actual": y_test.to_numpy(),
    "predicted": final_pred,
    "residual": final_errors,
}, index=y_test.index)
print(results.round(3))
print("final test MSE:", final_mse)
