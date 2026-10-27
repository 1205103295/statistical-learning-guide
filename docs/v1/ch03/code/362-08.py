influence = res_simple.get_influence()
diagnostics = pd.DataFrame({
    'leverage': influence.hat_matrix_diag,
    'studentized_residual': influence.resid_studentized_external,
    'cooks_distance': influence.cooks_distance[0],
}, index=data.index)
position = np.argmax(diagnostics['leverage'].to_numpy())
print('largest leverage position:', position)
print('corresponding data row:')
print(data.iloc[position])
print('largest Cook distances:')
print(diagnostics.sort_values('cooks_distance', ascending=False).head().round(4))
