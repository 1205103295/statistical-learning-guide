import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

image_dir = Path('图片')
image_dir.mkdir(exist_ok=True)
x_curve = np.linspace(-8.0, 8.0, 201)
p_curve = 1.0 / (1.0 + np.exp(-x_curve))
slope_curve = p_curve * (1.0 - p_curve)
fig, axes = plt.subplots(1, 2, figsize=(9, 3.5))
axes[0].plot(x_curve, p_curve, color='#314887')
axes[0].set(xlabel='x', ylabel='Probability', title='Intercept = 0, slope = 1')
axes[1].plot(x_curve, slope_curve, color='#24735A')
axes[1].set(xlabel='x', ylabel='Derivative', title='p(x) [1 - p(x)]')
fig.tight_layout()
fig.savefig(image_dir / '431-logistic.png', dpi=180)
plt.close(fig)
print(f'p(0) = {0.5:.2f}, derivative at 0 = {0.25:.2f}')
