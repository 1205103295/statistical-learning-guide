y_pred_linear = model.predict(X_test)
linear_test_mse = np.mean(
    (y_test_array - y_pred_linear) ** 2
)
print(y_pred_linear)
print(linear_test_mse)
