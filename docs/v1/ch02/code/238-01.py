numeric_columns = ["horsepower", "weight", "mpg"]
for column in numeric_columns:
    mean_value = clean[column].mean()
    print(column, mean_value)
