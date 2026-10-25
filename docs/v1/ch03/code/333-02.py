rng_noise = np.random.default_rng(17)
innovations = rng_noise.normal(size=100)
correlated = np.zeros(100)
correlated[0] = innovations[0]
for i in range(1, 100):
    correlated[i] = 0.8 * correlated[i-1] + 0.6 * innovations[i]
x_noise = np.linspace(0., 10., 100)
hetero = (0.2 + 0.3 * x_noise) * rng_noise.normal(size=100)
fig, axes = plt.subplots(1, 2, figsize=(8, 3.2))
axes[0].plot(correlated, color="#314887")
axes[0].set(xlabel="Time", ylabel="Simulated error", title="Correlated errors")
axes[1].scatter(x_noise, hetero, s=13, color="#24735A", alpha=0.7)
axes[1].set(xlabel="Input", ylabel="Simulated error", title="Changing error scale")
fig.tight_layout()
fig.savefig(image_dir / "333-noise.pdf")
fig.savefig(image_dir / "333-noise.png", dpi=180)
print("simulated observations:", len(correlated), len(hetero))
display(fig)
plt.close(fig)
