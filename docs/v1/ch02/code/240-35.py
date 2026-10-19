columns = ["displacement", "horsepower", "weight", "acceleration"]
axes = pd.plotting.scatter_matrix(auto_full[columns], figsize=(7.5, 7.5),
                                  alpha=0.4, s=9, diagonal="hist")
fig = axes[0, 0].figure
fig.tight_layout()
for suffix in ["pdf", "png"]:
    fig.savefig(image_dir / f"241-auto-matrix.{suffix}", dpi=180)
display(fig)
plt.close(fig)
