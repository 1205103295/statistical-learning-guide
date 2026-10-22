from pathlib import Path
import matplotlib.pyplot as plt
from IPython.display import display

image_dir = Path("图片")
image_dir.mkdir(exist_ok=True)
fig, ax = plt.subplots(figsize=(6.4, 4.0))
ax.scatter(x, y, label="Observed")
ax.plot(x, y_fit, label="Fitted line")
ax.set_xlabel("Advertising budget (thousand yuan)")
ax.set_ylabel("Sales (thousand units)")
ax.legend()
fig.tight_layout()
fig.savefig(image_dir / "311-fit.png", dpi=180)
fig.savefig(image_dir / "311-fit.pdf")
display(fig)
plt.close(fig)
