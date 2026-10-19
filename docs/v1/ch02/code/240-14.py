fig, axes = plt.subplots(1, 2, figsize=(9, 3.6))
axes[0].scatter(y_test, final_pred, s=20, alpha=0.7)
limits = [min(y_test.min(), final_pred.min()),
          max(y_test.max(), final_pred.max())]
axes[0].plot(limits, limits, "--", color="black")
axes[0].set(xlabel="Actual mpg", ylabel="Predicted mpg")
axes[1].scatter(final_pred, test_results["residual"], s=20, alpha=0.7)
axes[1].axhline(0, color="black", linestyle="--")
axes[1].set(xlabel="Predicted mpg", ylabel="Actual - predicted")
fig.tight_layout()
fig.savefig(image_dir / "240-test-diagnostics.pdf")
fig.savefig(image_dir / "240-test-diagnostics.png", dpi=180)
display(fig)
plt.close(fig)
