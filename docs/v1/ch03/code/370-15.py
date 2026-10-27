for page in range(2):
    fig, axes = plt.subplots(3, 2, figsize=(8, 9))
    for ax, name in zip(axes.flat, names15[page*6:(page+1)*6]):
        ax.scatter(b15[name], y15, s=8, alpha=.4)
        ax.set(xlabel=name, ylabel='crim')
    fig.tight_layout()
    fig.savefig(image_dir / f'ex15-scatter-{page+1}.png', dpi=160)
    plt.close(fig)
rows15 = []
for name in names15:
    if b15[name].nunique() <= 2:
        print(name, ': binary; powers duplicate, skip nonlinear test')
        continue
    centered = b15[name] - b15[name].mean()
    cubic = np.column_stack([np.ones(len(b15)), centered, centered**2, centered**3])
    fit15 = sm.OLS(y15, cubic).fit()
    test15 = anova_lm(simple15[name], fit15).iloc[1]
    rows15.append([name, test15['F'], test15['Pr(>F)']])
print(pd.DataFrame(rows15, columns=['variable','F_add_x2_x3','p']).to_string(index=False))
