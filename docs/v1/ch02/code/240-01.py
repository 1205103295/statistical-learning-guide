from pathlib import Path
import hashlib
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

data_dir = Path("数据")
image_dir = Path("图片")
result_dir = Path("结果")
for folder in [data_dir, image_dir, result_dir]:
    folder.mkdir(exist_ok=True)
