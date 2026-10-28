X_new = np.column_stack([
    np.ones(len(new_customers)),
    new_customers,
])
eta_multi = X_new @ beta_multi
print(X_new)
print('shapes:', X_new.shape, beta_multi.shape, eta_multi.shape)
