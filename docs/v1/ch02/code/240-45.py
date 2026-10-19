over7 = boston.loc[boston["rm"] > 7]
over8 = boston.loc[boston["rm"] > 8]
print("rm > 7:", len(over7), "rm > 8:", len(over8))
print(over8[["rm", "medv", "crim", "ptratio", "lstat"]].round(3).to_string())
summary8 = over8.agg(["min", "mean", "max"]).T
summary8.to_csv(result_dir / "boston_over8_summary.csv")
