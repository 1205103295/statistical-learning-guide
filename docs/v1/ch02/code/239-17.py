if chosen_method == "linear":
    final_model = LinearRegression()
    final_model.fit(X_dev, y_dev)
    final_pred = final_model.predict(X_test)
else:
    final_mean = y_dev.mean()
    final_pred = np.full(len(X_test), final_mean)

print(chosen_method)
print(final_pred)
