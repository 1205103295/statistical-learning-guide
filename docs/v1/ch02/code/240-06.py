train_table = X_train.copy()
train_table["mpg"] = y_train
print(train_table.describe().round(2))
