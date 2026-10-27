rm_errors = {}
for degree in [1, 2]:
    terms_rm = ['rm', 'lstat'] if degree == 1 else [
        poly('rm', degree=2, raw=True), 'lstat']
    design_rm = MS(terms_rm)
    train_rm = Boston.loc[train.index]
    valid_rm = Boston.loc[valid.index]
    fitted_rm = sm.OLS(train_rm['medv'],
                      design_rm.fit_transform(train_rm)).fit()
    prediction_rm = fitted_rm.predict(design_rm.transform(valid_rm))
    rm_errors[degree] = mean_squared_error(valid_rm['medv'], prediction_rm)
print('validation MSE by rm degree:', rm_errors)
print('selected degree:', min(rm_errors, key=rm_errors.get))
