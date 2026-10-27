final_design = make_design(best_name)
development_X = final_design.fit_transform(development)
final_result = sm.OLS(development['medv'], development_X).fit()
test_X = final_design.transform(test)
test_pred = final_result.predict(test_X)

test_mse = mean_squared_error(test['medv'], test_pred)
baseline_pred = np.full(len(test), development['medv'].mean())
baseline_mse = mean_squared_error(test['medv'], baseline_pred)

print('test MSE:', test_mse)
print('test RMSE:', np.sqrt(test_mse))
print('constant baseline MSE:', baseline_mse)
