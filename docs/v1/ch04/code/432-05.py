step = np.linalg.solve(H, grad)
beta_newton = beta - step
print('step:', np.round(step, 6))
print('beta after Newton step:', np.round(beta_newton, 6))
print('equation check:', np.allclose(H @ step, grad))
