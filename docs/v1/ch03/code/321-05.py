from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(features, y_multi)
new_markets = np.array([[50., 20.], [30., 10.]])
new_predictions = model.predict(new_markets)
print("intercept:", round(model.intercept_, 6))
print("coefficients:", np.round(model.coef_, 6))
print("new shapes:", new_markets.shape, new_predictions.shape)
print("new predictions:", np.round(new_predictions, 6))
