lowest = boston.loc[boston["medv"] == boston["medv"].min()]
print("zero-based row labels:", lowest.index.tolist())
print("one-based observation numbers:", (lowest.index + 1).tolist())
comparison = boston.agg(["min", "median", "max"]).T
for index, row in lowest.iterrows():
    comparison[f"row_{index}"] = row
print(comparison.round(3).to_string())
comparison.to_csv(result_dir / "boston_min_medv_comparison.csv")
