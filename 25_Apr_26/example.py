import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as plt
import warnings
warnings.filterwarnings("ignore")


df = pd.read_csv(
    r"D:\siddheshwar\Leanrbay_AI_course\machine_learning\25_Apr_26\25th_April_2026_Dataset\kidney_disease.csv"
)

print(df.head())

print(df.shape)

print(df.columns)
