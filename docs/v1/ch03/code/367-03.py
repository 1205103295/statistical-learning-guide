new_stores = Carseats.iloc[:2].drop(columns='Sales').copy()
new_store_X = design_carseats.transform(new_stores)
print(res_carseats.predict(new_store_X))
