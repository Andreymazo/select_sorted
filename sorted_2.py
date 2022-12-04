import csv
from itertools import islice
from operator import itemgetter
import pprint


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
        # ['15.12', '15.01', '14.51', '14.94', '14.96', '14.61', '14.56', '14.26', '13.95', '13.6']
        if not group_by_name:###Zdes ya ne ponimau kak rabotaet True False i chto nado sdelat
            with open('output.csv', "w") as f:
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
        # ['13.6', '13.95', '14.26', '14.51', '14.56', '14.61', '14.94', '14.96', '15.01', '15.12']
        for row in islice(reader, limit):  # first 10 put into Cache
            Cache[high_lst[index_1]] = get_columns(row)##V kachestve kluchei znachenia high iz high_lst
            index_1 += 1
        # print(Cache, end='\n')
        # return Cache, high_lst,


Cache = select_sorted(sort_columns='high', limit=10, order='desc', filename='dump.csv', group_by_name=True)


def poisk(limit=10):
    global srez
    name = []
    get_columns = itemgetter('date', 'open', 'high', 'low', 'close', 'volume', 'Name')
    with open('output_sorted_PCLN') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name.append(row['Name'])##Poluchaem spisok name, po nemu budem potom sortirovat(obrashatsya)
            # print(len(name))
    mass = {}
   # ['AAL', 'AAL', 'AAL', 'AAL', 'AAL']

    def perv_index(mass):#Naidem 1 index PCLN
        with open('output_sorted_PCLN') as csvfile:##Sortiruem po imeni PCLN Len obshii 619040
            reader = csv.DictReader(csvfile)
            index = 0
            # name = [str(x) for x in name]## Sozdali spisok 619040 elementov
            counter = 0
            for row in islice(reader, 619040):  # Skolko nado slozhim
                mass[index] = get_columns(row)  ##V kachestve kluchei словарь принимает только уникальные
                index += 1
                if mass[index - 1][6] == 'PCLN':  # Nashli 1 index PCLN 440062
                    return index

    index = perv_index(mass)
    print(index)
    print(len(mass))

            ##Nuzno mass sdelat polnim 619040, a ne 440062
    with open('output_sorted_PCLN') as csvfile:  ##Sortiruem po imeni PCLN Len obshii 619040
        reader = csv.DictReader(csvfile)
        index_1 = 0
        # name = [str(x) for x in name]## Sozdali spisok 619040 elementov
        counter = 0
        for row in islice(reader, 619040):  #
            mass[index_1] = get_columns(row)  ##V
            index_1 += 1
        print(len(mass))##619040

    def find_f(mass, index):  ##Funkciu s longreada vzyal
        ##Nahodim kolichestvo povtoriaushihsa imen znaya, chto pervii element na 440062 meste
        ###'PCLN': 1259
        freq = {}  # словарь для хранения частоты каждого элемента в списке

        # пространство поиска nums[left…right]
        print(index)
        index = index - 1###Eto ya proveril, kudato dva pervih index propali, nado vernut
        (left, right) = (index, len(mass) - 1)

        # цикл работает пока пространство поиска не будет исчерпано
        while left <= right:

            # если nums[left…right] состоит только из одного элемента, обновить его счетчик
            if mass[left][6] == mass[right][6]:
                freq[mass[left][6]] = freq.get(mass[left][6], 0) + (right - left + 1)

                # продолжаем поиск в nums[right+1… n-1] для nums[left]
                left = right + 1
                right = len(mass) - 1
            else:
                # уменьшить пространство поиска
                right = (left + right) // 2

        return freq

    freq = find_f(mass, index)
    print(freq)
    for k in freq:
        if k == 'PCLN':
            srez = int(freq[k])
            # print(srez)#1259
            # print(mass[440063])
            # print(index)
    sort_PCLN = {}#Zapishem v slovar 1259 znachenii PCLN

    for k in range(len(mass)):
        if index <= index + srez:
            sort_PCLN[k] = mass[index]
            index += 1
            keys = sort_PCLN[0]
            with open('out_PCLN.cvs', "w", newline='') as f:
                dict_writer = csv.DictWriter(f, keys)
                dict_writer.writeheader()
                dict_writer.writerow(sort_PCLN)###Pishet tolko 1 strochku, bolshego dobitsia  ne smog

poisk()
