import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.stats.anova import anova_lm
from ISLP import load_data
from ISLP.models import ModelSpec as MS
from pathlib import Path
image_dir = Path('图片')
image_dir.mkdir(exist_ok=True)

def report(result):
    table = pd.DataFrame({'coef': result.params, 'SE': result.bse,
                          't': result.tvalues, 'p': result.pvalues})
    print(table.to_string(float_format=lambda v: f'{v:.6g}'))
    print(f'R2={result.rsquared:.6f}, RSS={result.ssr:.6f}, '
          f'RSE={np.sqrt(result.scale):.6f}')
