new14 = pd.concat([data14, pd.DataFrame({'x1':[.1], 'x2':[.8]})], ignore_index=True)
y14_new = np.concatenate([y14, [6.]])
for name, columns in [('both',['x1','x2']), ('x1_only',['x1']), ('x2_only',['x2'])]:
    fit14 = sm.OLS(y14_new, sm.add_constant(new14[columns])).fit()
    inf14 = fit14.get_influence()
    print(name); report(fit14)
    print('new point h, external residual, Cook:',
          inf14.hat_matrix_diag[-1], inf14.resid_studentized_external[-1],
          inf14.cooks_distance[0][-1])
fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(x1, x2, s=16)
ax.scatter([.1], [.8], color='red', marker='x', s=80, label='Added point')
ax.set(xlabel='x1', ylabel='x2'); ax.legend()
fig.tight_layout(); fig.savefig(image_dir / 'ex14-collinearity.png', dpi=180)
plt.close(fig)
