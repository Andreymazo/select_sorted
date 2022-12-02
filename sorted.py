import csv
from itertools import islice
from operator import itemgetter
import pprint

New = {}


def select_sorted(sort_columns='high', order='asc', limit=10, filename='dump.csv', group_by_name=False):
    high_lst = []
    with open('all_stocks_5yr.csv', 'r', encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        group_by_name = []
        for row in reader:## Sozdali spisok is 10 elementov
            if len(high_lst) < limit:
                high_lst.append(row[sort_columns])
                group_by_name.append(row['Name'])
            else:
                break
        high_lst = [float(x) for x in high_lst]## pereveli iz str fo float
        group_by_name.sort()##Tut ispolsuu sort nechestno

        if not group_by_name:###Zdes ya ne ponimau kak rabotaet True False i chto nado sdelat
            with open('output.csv', "w") as f:
                writer = csv.writer(f)
                writer.writerow(group_by_name)
        else:

            for i in range(len(high_lst) - 1):  ##Sortiruem puzrkom
                index_1 = 0
                for j in range(len(high_lst) - index_1 - 1):
                    if high_lst[index_1] > high_lst[index_1 + 1]:
                        high_lst[index_1], high_lst[index_1 + 1] = high_lst[index_1 + 1], high_lst[index_1]
                        index_1 += 1
                    elif high_lst[index_1] < high_lst[index_1 + 1]:
                        index_1 += 1

                # with open('output.csv', "w") as f:
                #     writer = csv.writer(f)
                #     writer.writerow(group_by_name)

            if order == 'asc': ##Zanosim v cvs file po vozrastaniu
                with open('output.csv', "w") as f:
                    writer = csv.writer(f)
                    writer.writerow(high_lst)

            else:## ##Zanosim v cvs file po ubivaniu
                high_lst_revers = reversed(high_lst)
                with open('output.csv', "w") as f:
                    writer = csv.writer(f)
                    writer.writerow(list(high_lst_revers))


    get_columns = itemgetter('date','open','high','low','close','volume','Name')
    Cache = {}

    with open('all_stocks_5yr.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        index_1 = 0
        high_lst = [str(x) for x in high_lst]
        for row in islice(reader, limit):  # first 10 put into Cache
            Cache[high_lst[index_1]] = get_columns(row)##V kachestve kluchei znachenia high iz high_lst
            index_1 += 1
        print(Cache, end='\n')
        # return Cache, print(high_lst)
        # new = {}

        ## Obrashaemsya k elementu kortezha v slovare Cache: Cache[index_1]['high'] esli sovpal, to kortezh celicom stavim na 1 mesto
        new = {}
        index_1 = 0
        index_2 = 0
        for k in Cache:
            for v in Cache:
                if k == Cache[v][2]:
                    new.update({k: Cache[v]})
                    index_1 += 1
                elif k != Cache[v][2]:
                    index_1 += 1
                    index_2 += 1
                    # print(new)
        pprint.pprint(new, width=100)


select_sorted(sort_columns='high', limit=10, order='desc', filename='dump.csv', group_by_name=True)

# Cache, high_lst =
# def f(Cache):
#
#     print(Cache)
#
#
# f(Cache)

# def cache_new(func):
#     def wrapper(*args):
#         global New
#         if args[0] in New:
#             return New[0]
#         value = func(*args)
#         New[args[0]] = value
#         return value
#     return wrapper
#
#
# @cache_new