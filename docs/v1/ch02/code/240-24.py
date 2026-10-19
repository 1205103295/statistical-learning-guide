college_summary = college.describe().T
college_summary.to_csv(result_dir / "college_describe.csv")
basic_stats = ["count", "mean", "std", "min", "max"]
print(college_summary[basic_stats].round(2).to_string())
print("Private counts:", college["Private"].value_counts().to_dict())
