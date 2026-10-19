print(clean.loc[2, "horsepower"])
print(clean.iloc[2, 1])
horsepower_series = clean["horsepower"]
horsepower_table = clean[["horsepower"]]
print(horsepower_series.shape)
print(horsepower_table.shape)
