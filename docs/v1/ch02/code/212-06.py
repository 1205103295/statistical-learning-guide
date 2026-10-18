knn_model = KNeighborsRegressor(n_neighbors=2)
knn_model.fit(X_train, y_train)
