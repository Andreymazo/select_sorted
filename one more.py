import csv
import re
import os
import pandas as pd
import numpy as np

# df = pd.read_csv('all_stocks_5yr.csv')
# df.sort_values(by='Name', ascending=False, kind='heapsort')
# df.to_csv('output_sorted_PCLN')
# print(len(df))
# # DataFrame.sort_values(by, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None)
# index = 0
#for i in df:
    #if index < 10:
        # print(df)

#x = pd.Series(["PCLN", "2017-08-08"])
#a = list(x)
mass = []
# get_by_date():
with open('output_sorted_PCLN') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Name'] == 'PCLN' and row ['date'] == "2017-08-08":
            mass.append(row)
            print(mass)
with open('output.csv', "w") as f:
    writer = csv.writer(f)
    writer.writerow(mass)




# get_by_date(date="2017-08-08", name="PCLN", filename='dump.csv')



# # сохраняет в файл все данные по тикеры "PCLN" за 2017-08-08
# 2017-08-08 | 2044.0 | 2067.99 | 2035.11 | 2049.0 | 830572 | PCLN