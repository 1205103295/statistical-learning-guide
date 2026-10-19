cars_demo = pd.DataFrame({
    "horsepower": [160, 145, 135, 125, 115, 110,
                   105, 100, 90, 85, 75, 60],
    "weight": [4000, 3700, 3500, 3300, 3100, 3000,
               2900, 2800, 2600, 2400, 2200, 1800],
    "mpg": [15, 18, 19, 20, 21, 22,
            23, 24, 26, 28, 30, 45],
})
feature_columns = ["horsepower", "weight"]
target_column = "mpg"
X = cars_demo[feature_columns]
y = cars_demo[target_column]
print(X.shape, y.shape)
