X_dev, X_test, y_dev, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
X_train, X_val, y_train, y_val = train_test_split(
    X_dev, y_dev, test_size=0.25, random_state=24
)
print("train, validation, test:", len(X_train), len(X_val), len(X_test))
assert set(X_train.index).isdisjoint(X_val.index)
assert set(X_dev.index).isdisjoint(X_test.index)
split = pd.Series("train", index=clean_auto.index, name="split")
split.loc[X_val.index] = "validation"
split.loc[X_test.index] = "test"
split.to_csv(result_dir / "auto_split.csv", index_label="row_id")
