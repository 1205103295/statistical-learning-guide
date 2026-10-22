x_mean = x.mean()
y_mean = y.mean()
x_centered = x - x_mean
y_centered = y - y_mean
print("means:", x_mean, y_mean)
print("x_centered:", x_centered)
print("y_centered:", y_centered)
print("centered sums:", x_centered.sum(), y_centered.sum())
