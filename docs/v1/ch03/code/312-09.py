right_tail = t.sf(abs(t_obs), df=df)
p_value = 2 * right_tail
print(f"right tail = {right_tail:.6f}")
print(f"p = {p_value:.6f}")
