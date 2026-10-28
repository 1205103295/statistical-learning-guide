p_multi = 1.0 / (1.0 + np.exp(-eta_multi))
print('linear scores:', eta_multi)
print('probabilities:', np.round(p_multi, 6))
print(f'conditional student odds ratio = {np.exp(beta_multi[3]):.6f}')
