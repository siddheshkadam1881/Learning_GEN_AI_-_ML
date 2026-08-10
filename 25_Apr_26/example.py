# precheck here

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

#get all columns 
print(df.columns)



# get all columns repeat no.1
print(df.duplicated().sum())

# get all columns name and null count
print(df.isnull().sum())

# get all null counts dataframes
print(df.isnull().sum().sum())

print(df.info())


for i in df.columns:
    print("**********************************************")
    print(i)
    print(set(df[i].tolist()))
    print("**********************************************")



df['pcv'] = df['pcv'].replace(r'^\s*\?\s*$', np.nan, regex=True)

print(df['pcv'].mode()[0])

df['pcv'] = df['pcv'].apply(lambda x: '43' if pd.isna(x) else x)
print(df['pcv'].tolist())