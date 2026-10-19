auto = pd.read_csv(data_path, sep=r"\s+", na_values=["?"])
print(auto.shape)
print(auto.dtypes)
print(auto.isna().sum())
