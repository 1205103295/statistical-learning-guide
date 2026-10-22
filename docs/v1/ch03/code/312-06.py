for confidence in [0.90, 0.95, 0.99]:
    alpha_level = 1 - confidence
    critical = t.ppf(1 - alpha_level / 2, df=residual_df)
    half_width = critical * slope_se
    lower = beta1_hat - half_width
    upper = beta1_hat + half_width
    print(f"confidence={confidence:.0%}: [{lower:.3f}, {upper:.3f}]")
