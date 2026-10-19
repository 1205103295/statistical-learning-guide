from pathlib import Path
from urllib.request import urlopen
import hashlib
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_dir = Path("数据")
image_dir = Path("图片")
result_dir = Path("结果/教材章末习题")
for folder in [data_dir, image_dir, result_dir]:
    folder.mkdir(parents=True, exist_ok=True)
