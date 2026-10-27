b15 = load_data('Boston')
y15 = b15['crim']
names15 = b15.columns.drop('crim')
simple15 = {}
for name in names15:
    simple15[name] = sm.OLS(y15, sm.add_constant(b15[[name]])).fit()
full15 = sm.OLS(y15, sm.add_constant(b15[names15])).fit()
compare15 = pd.DataFrame({
    'simple_coef': [simple15[n].params[n] for n in names15],
    'simple_p': [simple15[n].pvalues[n] for n in names15],
    'multiple_coef': full15.params[names15],
    'multiple_p': full15.pvalues[names15]}, index=names15)
print(compare15.to_string(float_format=lambda v: f'{v:.5g}'))
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
for j, name in enumerate(names15):
    for ax in axes:
        ax.scatter(compare15.loc[name, 'simple_coef'],
                   compare15.loc[name, 'multiple_coef'],
                   color=plt.get_cmap('tab20')(j), label=name)
for ax in axes:
    ax.set(xlabel='Simple coefficient', ylabel='Multiple coefficient')
axes[0].set_title('Full range')
axes[1].set(xlim=(-3, 2), ylim=(-1.5, 1), title='Zoom near origin')
axes[1].legend(loc='center left', bbox_to_anchor=(1, 0.5))
fig.tight_layout(); fig.savefig(image_dir / 'ex15-coefficients.png', dpi=180)
plt.close(fig)
