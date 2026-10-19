from urllib.request import urlopen

source_url = "https://www.statlearning.com/s/Auto.data"
data_path = data_dir / "Auto.data"
if not data_path.exists():
    with urlopen(source_url, timeout=30) as response:
        data_path.write_bytes(response.read())
data_sha256 = hashlib.sha256(data_path.read_bytes()).hexdigest()
print(data_sha256)
