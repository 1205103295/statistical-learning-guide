from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

models = {
    "baseline": DummyRegressor(strategy="mean"),
    "linear": LinearRegression(),
    "knn5": make_pipeline(
        StandardScaler(), KNeighborsRegressor(n_neighbors=5)
    ),
}
