from ISLP import load_data
import ISLP

boston = load_data("Boston")
print("ISLP version:", ISLP.__version__)
print("shape:", boston.shape)
print("columns:", boston.columns.tolist())
boston.to_csv(result_dir / "boston_loaded.csv", index=False)
