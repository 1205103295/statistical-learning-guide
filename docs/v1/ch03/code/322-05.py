full_model = LinearRegression().fit(X_ads, y_ads)
reduced_model = LinearRegression().fit(X_reduced, y_ads)
rss_full = np.sum((y_ads - full_model.predict(X_ads)) ** 2)
rss_reduced = np.sum((y_ads - reduced_model.predict(X_reduced)) ** 2)
n_ads, p_full = X_ads.shape
p_reduced = X_reduced.shape[1]
k = p_full - p_reduced
nu_ads = n_ads - p_full - 1
f_partial = ((rss_reduced - rss_full) / k) / (rss_full / nu_ads)
p_partial = f.sf(f_partial, dfn=k, dfd=nu_ads)
print("RSS reduced, full:", np.round([rss_reduced, rss_full], 6))
print("df:", k, nu_ads)
print("F, p:", np.round([f_partial, p_partial], 6))
print("reject at 0.05:", bool(p_partial < 0.05))
