X_ads_design = np.column_stack((np.ones(n_ads), X_ads))
C_ads = np.linalg.solve(X_ads_design.T @ X_ads_design, np.eye(4))
z0 = np.array([1., 50., 9., 7.])
mu_hat = full_model.predict(z0[1:].reshape(1, -1))[0]
h0 = z0 @ C_ads @ z0
s_ads = np.sqrt(rss_full / nu_ads)
crit_ads = t.ppf(0.975, df=nu_ads)
se_mean = s_ads * np.sqrt(h0)
se_prediction = s_ads * np.sqrt(1 + h0)
ci_mean = mu_hat + np.array([-1., 1.]) * crit_ads * se_mean
pi_individual = mu_hat + np.array([-1., 1.]) * crit_ads * se_prediction
print("prediction, h0:", np.round([mu_hat, h0], 6))
print("mean interval:", np.round(ci_mean, 6))
print("individual interval:", np.round(pi_individual, 6))
