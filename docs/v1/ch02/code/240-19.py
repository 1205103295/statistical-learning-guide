training_error = 4.5 * (1 - flexibility) ** 2 + 0.1
curves = {"Squared bias": bias_squared,
          "Variance": variance, "Training error": training_error,
          "Test error": test_error, "Irreducible error": irreducible}
fig, ax = plt.subplots(figsize=(7, 4))
for label, values in curves.items():
    ax.plot(flexibility, values, label=label)
ax.set(xlabel="Flexibility", ylabel="Squared-error scale")
ax.legend(fontsize=9)
fig.tight_layout()
for suffix in ["pdf", "png"]:
    fig.savefig(image_dir / f"241-curves.{suffix}", dpi=180)
display(fig)
plt.close(fig)
