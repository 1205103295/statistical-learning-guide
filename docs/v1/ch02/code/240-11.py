from sklearn.base import clone

final_model = clone(models[chosen_name])
final_model.fit(X_dev, y_dev)
print("fixed method:", chosen_name)
print("development rows:", len(X_dev))
