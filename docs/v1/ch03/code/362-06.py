def abline(ax, intercept, slope, *args, **kwargs):
    x_limits = np.asarray(ax.get_xlim())
    y_limits = intercept + slope * x_limits
    ax.plot(x_limits, y_limits, *args, **kwargs)

fig, ax = plt.subplots(figsize=(7, 4))
ax.scatter(data['lstat'], y, s=18, alpha=0.55, color='steelblue')
abline(ax, res_simple.params['intercept'],
       res_simple.params['lstat'], 'r--', linewidth=2)
ax.set_xlabel('lstat (%)')
ax.set_ylabel('medv (thousand dollars)')
fig.tight_layout()
fig.savefig(image_dir / '362-fit.png', dpi=160)
plt.show()
plt.close(fig)
