student_or = np.exp(student_slope)
probability_difference = p_student[1] - p_student[0]
probability_ratio = p_student[1] / p_student[0]
print(f'odds ratio = {student_or:.6f}')
print(f'probability difference = {probability_difference:.6f}')
print(f'percentage-point difference = {100*probability_difference:.6f}')
print(f'probability ratio = {probability_ratio:.6f}')
