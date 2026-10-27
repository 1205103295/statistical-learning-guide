vif_values = []
for j in range(1, X_all.shape[1]):
    value = variance_inflation_factor(X_all.to_numpy(), j)
    vif_values.append(value)

vif_table = pd.DataFrame({'VIF': vif_values}, index=X_all.columns[1:])
print(vif_table.round(3))
