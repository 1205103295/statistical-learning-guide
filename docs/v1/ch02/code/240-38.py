columns = ["nox", "dis", "rm", "lstat", "medv"]
axes = pd.plotting.scatter_matrix(boston[columns], figsize=(8, 8),
                                  alpha=0.35, s=8, diagonal="hist")
diagonal = axes[0, 0]
labels = [f"{float(t.get_text()):g}" for t in diagonal.get_yticklabels()]
diagonal.set_yticks(diagonal.get_yticks(), labels=labels)
fig = axes[0, 0].figure
fig.tight_layout()
for suffix in ["pdf", "png"]:
    fig.savefig(image_dir / f"241-boston-matrix.{suffix}", dpi=180)
display(fig)
plt.close(fig)
