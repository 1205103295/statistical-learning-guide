features = ["horsepower", "weight", "year", "origin"]
fig, axes = plt.subplots(2, 2, figsize=(7, 6))
for ax, feature in zip(axes.flat, features):
    ax.scatter(auto_full[feature], auto_full["mpg"], s=10, alpha=0.45)
    ax.set(xlabel=feature, ylabel="mpg")
fig.tight_layout()
for suffix in ["pdf", "png"]:
    fig.savefig(image_dir / f"241-auto-mpg.{suffix}", dpi=180)
print(auto_full[quantitative].corr()["mpg"].drop("mpg").round(4))
display(fig)
plt.close(fig)
