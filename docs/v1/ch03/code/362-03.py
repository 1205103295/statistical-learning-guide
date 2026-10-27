model_simple = sm.OLS(y, X)
res_simple = model_simple.fit()

coef_table = pd.DataFrame({
    'coef': res_simple.params,
    'std_error': res_simple.bse,
    't': res_simple.tvalues,
    'p': res_simple.pvalues,
})
print(coef_table.to_string(float_format=lambda v: f'{v:.6g}'))
print('95% coefficient intervals:')
print(res_simple.conf_int(alpha=0.05).round(4))
