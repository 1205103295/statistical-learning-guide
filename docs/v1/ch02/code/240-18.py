flexibility = np.linspace(0, 1, 201)
bias_squared = 5 * (1 - flexibility) ** 2
variance = 4 * flexibility ** 2
irreducible = np.full_like(flexibility, 1.0)
test_error = bias_squared + variance + irreducible
training_error = 5 * (1 - flexibility) ** 2
