crime_corr = boston.corr(numeric_only=True)["crim"].drop("crim")
print(crime_corr.sort_values().round(4).to_string())
crime_corr.to_csv(result_dir / "boston_crime_correlations.csv")
