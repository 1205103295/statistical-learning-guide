auto_path = data_dir / "Auto.data"
if not auto_path.exists():
    auto_path.write_bytes(urlopen("https://www.statlearning.com/s/Auto.data",
                                  timeout=30).read())
auto_full = pd.read_csv(auto_path, sep=r"\s+", na_values="?").dropna().copy()
quantitative = ["mpg", "cylinders", "displacement", "horsepower",
                "weight", "acceleration", "year"]
print("complete rows:", len(auto_full))
print("origin codes:", sorted(auto_full["origin"].unique().tolist()))
