design_orth = MS([poly('lstat', degree=2), 'age'])
X_orth = design_orth.fit_transform(Boston)
res_orth = sm.OLS(Boston['medv'], X_orth).fit()
print('same fitted values:', np.allclose(res_quad.fittedvalues,
                                        res_orth.fittedvalues))
print('orthogonal basis coefficients:')
print(res_orth.params)
