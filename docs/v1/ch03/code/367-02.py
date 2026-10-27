all_variables = list(Carseats.columns.drop('Sales'))
terms_carseats = all_variables + [('Income', 'Advertising'), ('Price', 'Age')]
design_carseats = MS(terms_carseats)
X_carseats = design_carseats.fit_transform(Carseats)
res_carseats = sm.OLS(Carseats['Sales'], X_carseats).fit()

print('design columns:', list(X_carseats.columns))
print(pd.DataFrame({'coef': res_carseats.params, 'p': res_carseats.pvalues}))
