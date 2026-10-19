from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)
print(len(X_train), len(X_test))
print(X_train.index.to_list())
print(X_test.index.to_list())
