T = np.array([50., 50.])
R = np.array([0., 20.])
X_interaction = np.column_stack((np.ones(2), T, R, T * R))
b_interaction = np.array([5., 0.04, 0.10, 0.002])
interaction_predictions = X_interaction @ b_interaction
increase = (b_interaction[1] + b_interaction[3] * R) * 10
print("predictions:", interaction_predictions)
print("increase for TV +10:", increase)
