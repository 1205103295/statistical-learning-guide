from pathlib import Path
import matplotlib.pyplot as plt
from IPython.display import display
image_dir = Path("图片")
image_dir.mkdir(exist_ok=True)
rng = np.random.default_rng(42)
x_plot = np.linspace(0., 10., 25)
y_plot = 3 + 0.8 * x_plot + rng.normal(0, 1.5, size=25)
Xp = np.column_stack((np.ones(25), x_plot))
bp = np.linalg.lstsq(Xp, y_plot, rcond=None)[0]
sp = np.sqrt(np.sum((y_plot - Xp @ bp) ** 2) / 23)
grid = np.linspace(-2., 12., 100)
Zp = np.column_stack((np.ones(100), grid))
Cp = np.linalg.solve(Xp.T @ Xp, np.eye(2))
hp = np.sum((Zp @ Cp) * Zp, axis=1)
center = Zp @ bp
cp = t.ppf(0.975, df=23)
fig, ax = plt.subplots(figsize=(7, 4))
ax.fill_between(grid, center-cp*sp*np.sqrt(1+hp), center+cp*sp*np.sqrt(1+hp), color="#DFE8F4", label="Prediction interval")
ax.fill_between(grid, center-cp*sp*np.sqrt(hp), center+cp*sp*np.sqrt(hp), color="#A9C9BE", label="Mean confidence interval")
ax.plot(grid, center, color="#314887", label="Fitted mean")
ax.scatter(x_plot, y_plot, s=18, color="#314887")
ax.set(xlabel="Advertising budget", ylabel="Sales")
ax.legend(fontsize=8)
fig.tight_layout()
fig.savefig(image_dir / "322-intervals.pdf")
fig.savefig(image_dir / "322-intervals.png", dpi=180)
display(fig)
plt.close(fig)
