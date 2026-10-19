fig, axes = plt.subplots(1, 3, figsize=(8, 3.2))
for ax, feature in zip(axes, ["rad", "tax", "lstat"]):
    ax.scatter(boston[feature], boston["crim"], s=9, alpha=0.4)
    ax.set(xlabel=feature, ylabel="crim")
fig.tight_layout()
for suffix in ["pdf", "png"]:
    fig.savefig(image_dir / f"241-boston-crime.{suffix}", dpi=180)
display(fig)
plt.close(fig)
