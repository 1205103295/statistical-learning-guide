critical = norm.ppf(0.975)
coefficient_ci = np.array([
    beta_hat - critical * se,
    beta_hat + critical * se,
])
odds_ratio_ci = np.exp(coefficient_ci)
print('critical:', round(critical, 6))
print('coefficient CI:', np.round(coefficient_ci, 6))
print('odds ratio CI:', np.round(odds_ratio_ci, 6))
