mask = clean["weight"] <= 3000
selected = clean.loc[mask].copy()
X_selected = selected[feature_columns]
y_selected = selected[target_column]
print(selected)
print(X_selected.shape, y_selected.shape)
