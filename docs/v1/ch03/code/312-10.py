reject_null = p_value < alpha
critical_value = t.ppf(1 - alpha / 2, df=df)
margin = critical_value * slope_se
ci_lower = beta1_hat - margin
ci_upper = beta1_hat + margin
print("Reject H0:", reject_null)
print(f"CI = [{ci_lower:.6f}, {ci_upper:.6f}]")
