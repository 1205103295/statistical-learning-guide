for k in [1, 3]:
    neighbor_labels = y_knn[order[:k]]
    counts = pd.Series(neighbor_labels).value_counts()
    print("K =", k, "neighbors:", neighbor_labels.tolist())
    print("prediction:", counts.idxmax())
