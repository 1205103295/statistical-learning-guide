numeric9 = auto.select_dtypes(include='number')
pd.plotting.scatter_matrix(numeric9, figsize=(10, 10),
                           diagonal='hist', alpha=.35, s=8)
plt.tight_layout()
plt.savefig(image_dir / 'ex09-matrix.png', dpi=180)
plt.close('all')
print(numeric9.corr().round(3).to_string())
