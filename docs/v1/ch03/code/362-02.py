data = Boston[['lstat', 'medv']].dropna().copy()
y = data['medv']
X = pd.DataFrame({
    'intercept': np.ones(len(data)),
    'lstat': data['lstat'],
}, index=data.index)

assert X.index.equals(y.index)
assert X.notna().all().all() and y.notna().all()
print(X.head())
print('shapes:', X.shape, y.shape)
