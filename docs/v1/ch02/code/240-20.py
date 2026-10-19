X_knn = np.array([[0, 3, 0], [2, 0, 0], [0, 1, 3],
                  [0, 1, 2], [-1, 0, 1], [1, 1, 1]])
y_knn = np.array(["Red", "Red", "Red", "Green", "Green", "Red"])
distance = np.sqrt(np.sum(X_knn ** 2, axis=1))
order = np.argsort(distance)
print("distances:", np.round(distance, 4))
print("nearest observation numbers:", order + 1)
