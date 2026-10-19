river_count = int((boston["chas"] == 1).sum())
ratio_median = boston["ptratio"].median()
print("river-bordering areas:", river_count)
print("median pupil-teacher ratio:", ratio_median)
