values = clean["mpg"].to_numpy()
print(np.std(values, ddof=0))
print(np.std(values, ddof=1))
print(clean["mpg"].std())
