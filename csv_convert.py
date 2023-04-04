import pandas as pd
import numpy as np

df = pd.read_excel("data/thu_chi_19_2023.xlsx",index_col=0)
df.to_csv('data/thu_chi_csv.csv')
print (df.head(5))