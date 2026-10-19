columns = ["Top10perc", "Apps", "Enroll"]
axes = pd.plotting.scatter_matrix(college[columns], figsize=(7, 7),
                                  alpha=0.35, diagonal="hist", s=10)
fig = axes[0, 0].figure
fig.tight_layout()
for suffix in ["pdf", "png"]:
    fig.savefig(image_dir / f"241-college-matrix.{suffix}", dpi=180)
display(fig)
plt.close(fig)
