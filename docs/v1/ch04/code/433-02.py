eta_balance = balance_intercept + balance_slope * balance_new
p_balance = 1.0 / (1.0 + np.exp(-eta_balance))
print('linear scores:', eta_balance)
print('probabilities:', np.round(p_balance, 6))
print('percent:', np.round(100 * p_balance, 4))
