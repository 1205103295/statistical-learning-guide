bins = [10, 20, 30, 40, 50]
fig, ax = plt.subplots(figsize=(6, 4))
counts, edges, patches = ax.hist(
    mpg_demo, bins=bins, edgecolor="black", color="#8CA3CC"
)
ax.set_xlabel("Miles per gallon (mpg)")
ax.set_ylabel("Number of cars")
fig.tight_layout()
fig.savefig(image_dir / "239-hist.pdf")
fig.savefig(image_dir / "239-hist.png", dpi=180)
print(counts.astype(int))
display(fig)
plt.close(fig)
