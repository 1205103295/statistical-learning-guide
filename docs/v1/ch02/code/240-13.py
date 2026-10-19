test_results = pd.DataFrame({
    "name": clean_auto.loc[X_test.index, "name"],
    "actual": y_test,
    "predicted": final_pred,
}, index=X_test.index)
test_results["residual"] = (
    test_results["actual"] - test_results["predicted"]
)
print(test_results[["actual", "predicted", "residual"]].head().round(3))
test_results.to_csv(result_dir / "auto_test_predictions.csv",
                    index_label="row_id")
