rng14 = np.random.default_rng(10)
x1 = rng14.uniform(0, 1, size=100)
x2 = .5 * x1 + rng14.normal(size=100) / 10
y14 = 2 + 2 * x1 + .3 * x2 + rng14.normal(size=100)
data14 = pd.DataFrame({'x1': x1, 'x2': x2})
print('correlation:', np.corrcoef(x1, x2)[0, 1])
models14 = {}
for name, columns in [('both', ['x1','x2']), ('x1_only',['x1']), ('x2_only',['x2'])]:
    models14[name] = sm.OLS(y14, sm.add_constant(data14[columns])).fit()
    print(name); report(models14[name])
