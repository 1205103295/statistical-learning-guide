for column in numeric_columns:
    mean_value = clean[column].mean()
    print(f"{column}: {mean_value:.2f}")

for column in numeric_columns:
    min_value = clean[column].min()
    max_value = clean[column].max()
    print(column, min_value, max_value)
