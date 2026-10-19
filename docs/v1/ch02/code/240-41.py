boston_ranges = boston.agg(["min", "median", "max"]).T
print(boston_ranges.round(4).to_string())
boston_ranges.to_csv(result_dir / "boston_ranges.csv")
