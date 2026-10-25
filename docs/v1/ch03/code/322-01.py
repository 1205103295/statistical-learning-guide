from scipy.stats import t, f
n, q = X.shape
df_resid = n - q
C = np.linalg.solve(X.T @ X, np.eye(q))
s2_multi = rss_multi / df_resid
se_multi = np.sqrt(s2_multi * np.diag(C))
t_values = coef_ls / se_multi
p_values = 2 * t.sf(np.abs(t_values), df=df_resid)
critical = t.ppf(0.975, df=df_resid)
ci_multi = np.column_stack((coef_ls - critical * se_multi,
                            coef_ls + critical * se_multi))
print("df, s2:", df_resid, round(s2_multi, 6))
print("standard errors:", np.round(se_multi, 6))
print("t values:", np.round(t_values, 6))
print("p values:", np.round(p_values, 6))
print("95% intervals:\n", np.round(ci_multi, 6))
