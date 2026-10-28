fig, ax = plt.subplots(figsize=(6, 3.5))
ax.bar(['Initial', 'Gradient step', 'Newton step'], losses,
       color=['#A6AAB5', '#314887', '#24735A'])
ax.set(ylabel='Mean negative log-likelihood', ylim=(0, 0.8))
for index, value in enumerate(losses):
    ax.text(index, value + 0.01, f'{value:.4f}', ha='center')
fig.tight_layout()
fig.savefig(image_dir / '432-loss-steps.png', dpi=180)
plt.close(fig)
print('Saved comparison of one update from the same initial parameters.')
