from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

project_data = Boston[['lstat', 'age', 'medv']].dropna().copy()
development, test = train_test_split(project_data, test_size=0.2, random_state=42)
train, valid = train_test_split(development, test_size=0.25, random_state=42)
print('train, valid, test:', len(train), len(valid), len(test))
