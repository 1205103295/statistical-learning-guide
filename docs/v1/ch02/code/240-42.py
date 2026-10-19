for column in ["crim", "tax", "ptratio"]:
    largest = boston.nlargest(3, column)[[column]]
    print("Top 3 by", column)
    print(largest.to_string())
