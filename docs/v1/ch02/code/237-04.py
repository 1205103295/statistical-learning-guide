feature_columns = ["horsepower", "weight"]
target_column = "mpg"
required_columns = feature_columns + [target_column]
clean = df.dropna(subset=required_columns).copy()
print(clean)
