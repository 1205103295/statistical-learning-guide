true_mean = 2.0 + 3.0 * x
error_a = np.array([-1.0, 0.0, 1.0])
error_b = np.array([1.0, 0.0, -1.0])

for name, errors in [("A", error_a), ("B", error_b)]:
    y_case = true_mean + errors
    slope_case = np.sum(x_centered * (y_case - y_case.mean())) / Sxx
    intercept_case = y_case.mean() - slope_case * x_mean
    rss_case = np.sum((y_case - (intercept_case + slope_case * x)) ** 2)
    print(name, "sales:", y_case)
    print("slope, intercept, RSS:", slope_case, intercept_case, rss_case)
