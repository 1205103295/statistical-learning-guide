rng12 = np.random.default_rng(12)
x12 = rng12.normal(size=100)
y12 = 2 * x12 + rng12.normal(size=100)
print('different:', (x12 @ y12) / (x12 @ x12),
      (x12 @ y12) / (y12 @ y12))
u12 = rng12.normal(size=100)
v12 = .5 * u12 + rng12.normal(size=100)
v12 = v12 * np.linalg.norm(u12) / np.linalg.norm(v12)
print('same:', (u12 @ v12) / (u12 @ u12),
      (u12 @ v12) / (v12 @ v12))
