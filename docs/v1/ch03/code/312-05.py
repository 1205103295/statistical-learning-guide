margin = critical_value * slope_se
ci_lower = beta1_hat - margin
ci_upper = beta1_hat + margin
print("estimated slope:", beta1_hat)
print("margin:", margin)
print("95% interval:", ci_lower, ci_upper)
