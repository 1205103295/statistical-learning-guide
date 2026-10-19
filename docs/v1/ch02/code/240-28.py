college["Elite"] = pd.cut(college["Top10perc"], bins=[0, 50, 100],
                          labels=["No", "Yes"], include_lowest=True)
assert college["Elite"].notna().all()
assert (college["Elite"] == "Yes").equals(college["Top10perc"] > 50)
print(college["Elite"].value_counts().to_string())
