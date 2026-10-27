design_two = MS(['lstat', 'age'])
X_two = design_two.fit_transform(Boston)
res_two = sm.OLS(Boston['medv'], X_two).fit()
print(pd.DataFrame({'coef': res_two.params, 'p': res_two.pvalues}))
