learning_rate = 0.6
beta_gradient = beta - learning_rate * grad
p_gradient = 1.0 / (1.0 + np.exp(-(X @ beta_gradient)))
loss_before = -np.mean(y * np.log(p) + (1-y) * np.log(1-p))
loss_gradient = -np.mean(
    y * np.log(p_gradient) + (1-y) * np.log(1-p_gradient)
)
print('beta after gradient step:', np.round(beta_gradient, 6))
print('probabilities:', np.round(p_gradient, 6))
print(f'loss before = {loss_before:.6f}')
print(f'loss after = {loss_gradient:.6f}')
