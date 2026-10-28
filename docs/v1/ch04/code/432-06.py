candidates = [
    ('initial', beta),
    ('gradient', beta_gradient),
    ('newton', beta_newton),
]
losses = []
for name, current_beta in candidates:
    current_eta = X @ current_beta
    current_p = 1.0 / (1.0 + np.exp(-current_eta))
    current_loss = -np.mean(
        y * np.log(current_p) + (1-y) * np.log(1-current_p)
    )
    losses.append(current_loss)
    print(name, np.round(current_beta, 6), f'loss = {current_loss:.6f}')
p_newton = 1.0 / (1.0 + np.exp(-(X @ beta_newton)))
grad_newton = X.T @ (p_newton - y) / n
print('gradient after Newton:', np.round(grad_newton, 6))
