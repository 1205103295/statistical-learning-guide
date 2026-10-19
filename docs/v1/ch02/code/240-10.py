chosen_name = scores["validation_mse"].idxmin()
print("chosen:", chosen_name)
print("training target mean:", y_train.mean())
scaler = models["knn5"].named_steps["standardscaler"]
print("scaler mean:", scaler.mean_)
print("scaler scale:", scaler.scale_)
assert np.allclose(scaler.mean_, X_train.mean().to_numpy())
assert np.allclose(scaler.scale_, X_train.std(ddof=0).to_numpy())
