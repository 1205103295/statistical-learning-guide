design_interaction = MS(['lstat', 'age', ('lstat', 'age')])
X_interaction = design_interaction.fit_transform(Boston)
res_interaction = sm.OLS(Boston['medv'], X_interaction).fit()
print(pd.DataFrame({'coef': res_interaction.params,
                    'p': res_interaction.pvalues}))
