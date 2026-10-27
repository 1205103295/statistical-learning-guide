Auto = load_data('Auto')
auto = Auto.dropna().copy()
y8 = auto['mpg']
X8 = sm.add_constant(auto[['horsepower']])
r8 = sm.OLS(y8, X8).fit()
print('rows:', len(auto))
report(r8)
new8 = pd.DataFrame({'const': [1.], 'horsepower': [98.]})
print(r8.get_prediction(new8).summary_frame().round(4).to_string())
