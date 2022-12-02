import csv
import re
import os
import pandas as pd
import numpy as np

df = pd.read_csv('all_stocks_5yr.csv')
df.sort_values(by='high', ascending=False, kind='heapsort')
print(len(df))
# DataFrame.sort_values(by, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None)
index = 0
for i in df:
    if index < 10:
        print(df)