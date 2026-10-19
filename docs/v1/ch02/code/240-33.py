auto_stats = auto_full[quantitative].agg(["min", "max", "mean", "std"]).T
auto_stats["span"] = auto_stats["max"] - auto_stats["min"]
print(auto_stats.round(3).to_string())
auto_stats.to_csv(result_dir / "auto_full_summary.csv")
