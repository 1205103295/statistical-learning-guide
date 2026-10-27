rng11 = np.random.default_rng(1)
x11 = rng11.normal(size=100)
y11 = 2 * x11 + rng11.normal(size=100)
for name, response, predictor in [('y_on_x', y11, x11), ('x_on_y', x11, y11)]:
    fitted11 = sm.OLS(response, predictor).fit()
    print(name, 'without intercept')
    report(fitted11)
    with_intercept = sm.OLS(response, sm.add_constant(predictor)).fit()
    print('with intercept slope t:', with_intercept.tvalues[1])
A11 = x11 @ x11; B11 = y11 @ y11; C11 = x11 @ y11
t11 = np.sqrt(99) * C11 / np.sqrt(A11 * B11 - C11 ** 2)
print('derived t:', t11)
