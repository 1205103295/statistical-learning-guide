fig, axes = plt.subplots(2, 2, figsize=(7, 6))
settings = [("Apps", 10), ("Apps", 30), ("Outstate", 15), ("Expend", 30)]
for ax, (column, bins) in zip(axes.flat, settings):
    college[column].plot.hist(bins=bins, ax=ax, edgecolor="white")
    ax.set(title=f"{column}: {bins} bins", xlabel=column)
fig.tight_layout()
for suffix in ["pdf", "png"]:
    fig.savefig(image_dir / f"241-college-hist.{suffix}", dpi=180)
display(fig)
plt.close(fig)
