from scipy.stats import t

alpha = 0.05
left_probability = 1 - alpha / 2
critical_value = t.ppf(left_probability, df=residual_df)
print("alpha:", alpha)
print("left cumulative probability:", left_probability)
print("critical value:", critical_value)
