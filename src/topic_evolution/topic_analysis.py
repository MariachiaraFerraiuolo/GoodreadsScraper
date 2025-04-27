import pandas as pd
import sys
import os

file_path = r'output\lemmatized_data.xlsx'

df = pd.read_excel(file_path)
df['year_group'] = pd.cut(df['year'], bins=[2003, 2010, 2015, 2020, 2025], labels=['2004-10', '2010-15', '2015-20', '2020-25'])
print(df)
print(df[df['year']==2004])
print(df.columns)