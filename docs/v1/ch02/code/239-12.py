y_train_pred = model.predict(X_train)
y_train_array = y_train.to_numpy()
residual_train = y_train_array - y_train_pred
print(np.round(residual_train, 3))
print(np.mean(residual_train ** 2))
