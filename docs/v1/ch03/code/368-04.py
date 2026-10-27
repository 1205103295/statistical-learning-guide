prediction_table.to_csv('简单回归_预测区间.csv', index=False)
vif_table.to_csv('全变量模型_VIF.csv', index=True)

import importlib.metadata as metadata
for package in ['numpy', 'pandas', 'statsmodels', 'ISLP', 'scikit-learn']:
    print(package, metadata.version(package))
