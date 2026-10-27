inf9 = r9.get_influence()
diag9 = pd.DataFrame({'studentized': inf9.resid_studentized_external,
                     'leverage': inf9.hat_matrix_diag}, index=auto.index)
print('largest absolute studentized residuals:')
print(diag9.loc[diag9['studentized'].abs().nlargest(3).index].round(4))
print('largest leverage:')
print(diag9.nlargest(3, 'leverage').round(4))
fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(r9.fittedvalues, r9.resid, s=12, alpha=.5)
ax.axhline(0, color='black', linestyle='--')
ax.set(xlabel='Fitted mpg', ylabel='Residual')
fig.tight_layout(); fig.savefig(image_dir / 'ex09-residual.png', dpi=180)
plt.close(fig)
for name, values in {
    'hp_weight': auto['horsepower'] * auto['weight'],
    'weight_year': auto['weight'] * auto['year'],
    'hp_squared': auto['horsepower'] ** 2,
    'hp_log': np.log(auto['horsepower']),
    'hp_sqrt': np.sqrt(auto['horsepower']),
}.items():
    extended = X9.copy()
    extended[name] = values
    fitted9 = sm.OLS(auto['mpg'], extended).fit()
    print(name, 'p=', f'{fitted9.pvalues[name]:.6g}',
          'adjusted R2=', round(fitted9.rsquared_adj, 6))
