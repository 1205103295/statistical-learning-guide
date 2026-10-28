threshold = 0.5
y_pred = (p_balance >= threshold).astype(int)
boundary = -balance_intercept / balance_slope
print('comparison:', p_balance >= threshold)
print('predicted classes:', y_pred)
print(f'balance boundary = {boundary:.1f}')
