def make_design(name):
    if name == 'linear':
        return MS(['lstat', 'age'])
    if name == 'quadratic':
        return MS([poly('lstat', degree=2, raw=True), 'age'])
    raise ValueError('Unknown model name')

validation_errors = {}
for name in ['linear', 'quadratic']:
    design = make_design(name)
    train_X = design.fit_transform(train)
    fitted = sm.OLS(train['medv'], train_X).fit()
    valid_X = design.transform(valid)
    valid_pred = fitted.predict(valid_X)
    validation_errors[name] = mean_squared_error(valid['medv'], valid_pred)

print(pd.Series(validation_errors, name='validation MSE'))
best_name = min(validation_errors, key=validation_errors.get)
print('selected:', best_name)
