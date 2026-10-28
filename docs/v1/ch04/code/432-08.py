from scipy.stats import norm

beta_hat = 0.4049
se = 0.1150
z = beta_hat / se
p_value = 2.0 * norm.sf(abs(z))
print(f'z = {z:.6f}')
print(f'p-value = {p_value:.8f}')
