feature_names = ["TV", "radio", "newspaper"]
vif_values = []
for j, name in enumerate(feature_names):
    target = X_ads[:, j]
    other_features = np.delete(X_ads, j, axis=1)
    auxiliary = LinearRegression().fit(other_features, target)
    r2_aux = auxiliary.score(other_features, target)
    vif = 1 / (1 - r2_aux)
    vif_values.append(vif)
    print(name, "auxiliary R2, VIF:", np.round([r2_aux, vif], 6))
