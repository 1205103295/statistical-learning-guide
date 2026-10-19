fig, axes = plt.subplots(1, 2, figsize=(9, 3.6))
for ax, feature in zip(axes, feature_columns):
    ax.scatter(X_train[feature], y_train, s=17, alpha=0.6,
               color="#314887")
    ax.set_xlabel(feature)
    ax.set_ylabel("mpg")
fig.tight_layout()
fig.savefig(image_dir / "240-train-scatter.pdf")
fig.savefig(image_dir / "240-train-scatter.png", dpi=180)
display(fig)
plt.close(fig)
