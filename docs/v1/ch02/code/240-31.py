print(college[["Apps", "Expend"]].agg(["mean", "median"]).round(2))
print("Apps-Enroll correlation:", round(college["Apps"].corr(college["Enroll"]), 4))
unusual = college.loc[college["Grad.Rate"] > 100, ["Grad.Rate"]]
print("Graduation rate above 100:")
print(unusual.to_string())
