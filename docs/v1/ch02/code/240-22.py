college_path = data_dir / "College.csv"
college_url = "https://www.statlearning.com/s/College.csv"
if not college_path.exists():
    college_path.write_bytes(urlopen(college_url, timeout=30).read())
college_raw = pd.read_csv(college_path)
print("raw shape:", college_raw.shape)
print(college_raw.iloc[:3, :4].to_string(index=False))
