import csv
from itertools import islice
from operator import itemgetter

def select_sorted(sort_columns='high', order='asc', limit=10, filename='dump.csv', group_by_name=False):
    high_lst = []
    with open('all_stocks_5yr.csv', 'r', encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')

        group_by_name = []
        for row in reader:## Sozdali spisok is 10 elementov
            if len(high_lst) <= limit:
                high_lst.append(row[sort_columns])
                group_by_name.append(row['Name'])
            else:
                break
        high_lst = [float(x) for x in high_lst]## pereveli iz str fo float
        group_by_name.sort()##Tut ispolsuu sort nechestno
        if not group_by_name:###Zdes ya ne ponimau kak rabotaet True False i chto nado sdelat
            with open(filename, "w") as f:
                writer = csv.writer(f)
                writer.writerow(group_by_name)
        else:

            for i in range(len(high_lst) - 1):  ##Sortiruem puzrkom
                index_1 = 0
                for j in range(len(high_lst) - 1):
                    if high_lst[index_1] > high_lst[index_1 + 1]:
                        high_lst[index_1], high_lst[index_1 + 1] = high_lst[index_1 + 1], high_lst[index_1]
                        index_1 += 1
                    elif high_lst[index_1] < high_lst[index_1 + 1]:
                        index_1 += 1

            if order == 'asc': ##Zanosim v cvs file po vozrastaniu
                with open(filename, "w") as f:
                    writer = csv.writer(f)
                    writer.writerow(high_lst)

            else:## ##Zanosim v cvs file po ubivaniu
                high_lst_revers = reversed(high_lst)
                with open(filename, "w") as f:
                    writer = csv.writer(f)
                    writer.writerow(list(high_lst_revers))

    get_columns = itemgetter('Name', 'open', 'volume', 'close', 'low')
    Cache = {}

    with open('all_stocks_5yr.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        index_1 = 0
        for row in islice(reader, 10):  # first 10 put into Cache
            index_2 = 0
            for i in high_lst:
                Cache[high_lst[index_2]] = get_columns(row)
                index_2 += 1
            index_1 += 1
        print(Cache, end='\n')

select_sorted(sort_columns='high', limit=20, order='desc', filename='dump.csv', group_by_name=True)
