feature_columns = ["horsepower", "weight"]
target_column = "mpg"
required = feature_columns + [target_column]
clean_auto = auto.dropna(subset=required).copy()
X = clean_auto[feature_columns]
y = clean_auto[target_column]
print("raw, complete, removed:", len(auto), len(X), len(auto)-len(X))
print(X.shape, y.shape)
assert X.index.equals(y.index)
assert X.notna().all().all() and y.notna().all()
