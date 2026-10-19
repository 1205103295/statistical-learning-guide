report = {
    "source": source_url, "sha256": data_sha256,
    "features": feature_columns, "target": target_column,
    "n_raw": len(auto), "n_complete": len(clean_auto),
    "n_train": len(X_train), "n_validation": len(X_val),
    "n_test": len(X_test), "seeds": [42, 24],
    "selected_method": chosen_name,
    "test_mse": float(test_mse), "test_rmse": float(test_rmse),
    "test_mae": float(test_mae),
    "baseline_test_mse": float(baseline_test_mse),
}
report_path = result_dir / "auto_report.json"
report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
print("Saved:", report_path.as_posix())
