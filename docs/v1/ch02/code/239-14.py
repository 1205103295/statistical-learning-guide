X_dev, X_test, y_dev, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)
X_train, X_val, y_train, y_val = train_test_split(
    X_dev, y_dev, test_size=1/3, random_state=42
)
print(len(X_train), len(X_val), len(X_test))
print(X_train.index.to_list())
print(X_val.index.to_list())
print(X_test.index.to_list())
assert set(X_train.index).isdisjoint(X_val.index)
assert set(X_dev.index).isdisjoint(X_test.index)
