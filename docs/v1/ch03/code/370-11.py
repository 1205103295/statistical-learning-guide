rng13 = np.random.default_rng(1)
x13 = rng13.normal(size=100)
z13 = rng13.normal(size=100)
X13 = sm.add_constant(x13)
rows13 = []
fig, axes = plt.subplots(1, 3, figsize=(12, 3.6))
for ax, sigma in zip(axes, [.25, .5, 1.]):
    eps13 = sigma * z13
    y13 = -1 + .5 * x13 + eps13
    fitted13 = sm.OLS(y13, X13).fit()
    ci13 = fitted13.conf_int()
    rows13.append([sigma, *fitted13.params, *ci13[0], *ci13[1]])
    ax.scatter(x13, y13, s=10, alpha=.5)
    gx = np.array([x13.min(), x13.max()])
    ax.plot(gx, -1 + .5 * gx, color='black', label='True mean')
    ax.plot(gx, fitted13.params[0] + fitted13.params[1] * gx,
            color='red', linestyle='--', label='OLS')
    ax.set(title=f'noise SD={sigma}', xlabel='x', ylabel='y')
    ax.legend(fontsize=8)
table13 = pd.DataFrame(rows13, columns=['sigma','b0','b1','b0_low','b0_high','b1_low','b1_high'])
print(table13.round(5).to_string(index=False))
fig.tight_layout(); fig.savefig(image_dir / 'ex13-noise.png', dpi=180)
plt.close(fig)
y13_base = -1 + .5 * x13 + .5 * z13
quad13 = sm.OLS(y13_base, np.column_stack([np.ones(100), x13, x13 ** 2])).fit()
print('base quadratic p:', quad13.pvalues[2])
