new_car = pd.DataFrame({"horsepower": [100.0], "weight": [3000.0]})
new_prediction = final_model.predict(new_car)
print("predicted mpg:", np.round(new_prediction, 3))
