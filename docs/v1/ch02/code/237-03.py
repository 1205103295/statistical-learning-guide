df.info()
print(df.isna())
missing_counts = df.isna().sum(axis=0)
print(missing_counts)
