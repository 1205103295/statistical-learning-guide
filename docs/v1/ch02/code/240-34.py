keep = np.ones(len(auto_full), dtype=bool)
keep[9:85] = False
auto_subset = auto_full.iloc[keep].copy()
subset_stats = auto_subset[quantitative].agg(["min", "max", "mean", "std"]).T
subset_stats["span"] = subset_stats["max"] - subset_stats["min"]
print("removed:", (~keep).sum(), "remaining:", len(auto_subset))
print(subset_stats.round(3).to_string())
subset_stats.to_csv(result_dir / "auto_subset_summary.csv")
