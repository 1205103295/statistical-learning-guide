y_val_array = y_val.to_numpy()
baseline_val_mse = np.mean(
    (y_val_array - baseline_val_pred) ** 2
)
linear_val_mse = np.mean(
    (y_val_array - linear_val_pred) ** 2
)
chosen_method = (
    "linear" if linear_val_mse < baseline_val_mse
    else "baseline"
)
print("baseline validation MSE:", baseline_val_mse)
print("linear validation MSE:", linear_val_mse)
print("chosen:", chosen_method)
