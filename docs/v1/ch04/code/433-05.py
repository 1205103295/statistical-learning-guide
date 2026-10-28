eta_student = student_intercept + student_slope * student
p_student = 1.0 / (1.0 + np.exp(-eta_student))
print('linear scores:', eta_student)
print('probabilities:', np.round(p_student, 6))
