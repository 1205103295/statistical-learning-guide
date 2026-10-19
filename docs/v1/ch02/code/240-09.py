rows = []
for name, candidate in models.items():
    candidate.fit(X_train, y_train)
    train_pred = candidate.predict(X_train)
    val_pred = candidate.predict(X_val)
    rows.append({
        "model": name,
        "train_mse": mean_squared_error(y_train, train_pred),
        "validation_mse": mean_squared_error(y_val, val_pred),
    })
scores = pd.DataFrame(rows).set_index("model")
print(scores.round(4))
scores.to_csv(result_dir / "auto_validation_scores.csv")
