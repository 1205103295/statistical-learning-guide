baseline_value = y_train.mean()
baseline_pred = np.full(
    shape=len(X_test), fill_value=baseline_value
)
print(baseline_value)
print(baseline_pred)
print(baseline_pred.shape)
