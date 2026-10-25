n_demo, p_demo = 20, 3
rss_null, rss_full_demo = 100.0, 40.0
df_num = p_demo
df_den = n_demo - p_demo - 1
f_demo = ((rss_null - rss_full_demo) / df_num) / (rss_full_demo / df_den)
p_demo_value = f.sf(f_demo, dfn=df_num, dfd=df_den)
f_critical = f.ppf(0.95, dfn=df_num, dfd=df_den)
r2_demo = 1 - rss_full_demo / rss_null
f_from_r2 = (r2_demo / p_demo) / ((1 - r2_demo) / df_den)
assert np.isclose(f_demo, f_from_r2)
print("F, p, critical:", np.round([f_demo, p_demo_value, f_critical], 6))
print("R2, F from R2:", np.round([r2_demo, f_from_r2], 6))
