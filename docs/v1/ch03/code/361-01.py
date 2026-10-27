import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from ISLP import load_data
from ISLP.models import ModelSpec as MS, poly
from pathlib import Path

image_dir = Path('图片')
image_dir.mkdir(exist_ok=True)
