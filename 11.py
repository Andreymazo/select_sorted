import csv
from itertools import islice
from operator import itemgetter
import pprint


def dec_cache(func):
    cache = {}

    def wrapper(dic):
        if dic[0] in cache:
            return dic[0]
        value = func(dic)
        cache[0] = value
        return value

    return wrapper


@dec_cache
def sort_smth(dic):  ###Минимальное число справа и проверка на отсортированность counter = 0
    # counter счетчик заменыб если нуль, то отсортирован
    #####Сначала пробежим и найдем наименьший элемент
    result = False
    while not result:  # Сюда надо снова подать будет список после его сортировки пополам, т.е. high из функции f_3

        index = 0
        counter = 0
        for i in range(len(dic)-1):
            try:
                # print(high)
                # if high[index] < high[index + 1] and index==len(high):
                #     index = 0
                if dic[index] < dic[index + 1]:
                    dic[index], dic[index + 1] = dic[index + 1], dic[index]  ###Наименьший элемент в конце цикла окажется на последнем месте
                    index += 1
                    counter += 1
                    # print(counter, high)
                elif dic[index] > dic[index + 1]:
                    index += 1
                elif dic[index] == dic[index + 1]:
                    #     ost.append(high[index])  ##Дубликат заносим в ost
                    #     high.remove(high[index])  ##Дубликат убираем
                    index += 1
                #     counter += 1
                if counter == 0 and index == len(dic) - 1:  ##Услловие выхода из прогграммы, весь список отсортирован, ni odnogo izmenenia ne proizoshlo
                    # print(counter, high)
                    result = True  ## V etoi tochke dolzhen bit otsortirovannii spisok high i spisok ost s duplicarami
                    break  # No pochemu to go konca nedosortirovivaet

            except IndexError:
                pass
            continue

    return dic


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
        get_columns = itemgetter('date', 'open', 'high', 'low', 'close', 'volume', 'Name')
        Cache = {}

        with open('all_stocks_5yr.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            index_1 = 0
            high_lst = [float(x) for x in high_lst]
            sort_smth(high_lst)#sortiruem
            high_lst = [str(x) for x in high_lst]#Perevodim obratno v str
            # ['13.6', '13.95', '14.26', '14.51', '14.56', '14.61', '14.94', '14.96', '15.01', '15.12']
            for row in islice(reader, limit):  # first 10 put into Cache
                Cache[high_lst[index_1]] = get_columns(row)  ##V kachestve kluchei znachenia high iz high_lst
                index_1 += 1

            # print(high_lst)

            # print(Cache)

            # sort_smth(group_by_name)
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
            #pprint.pprint(new, width=100)#slovar new otsortirovan
            return new
Cache = select_sorted(sort_columns='high', limit=10, order='desc', filename='dump.csv', group_by_name=True)




        #################Potom zapishem#######################
        # with open('output.csv', "w") as f:
        #     writer = csv.writer(f)
        #     writer.writerow(group_by_name)
        ########################################
        # index = 0
        # for i in high_lst:
        #     if index < 10:
        #         print(i)
        #         index += 1

       # ['15.12', '15.01', '14.51', '14.94', '14.96', '14.61', '14.56', '14.26', '13.95', '13.6']

        #sort_smth(high_lst)
        # index = 0
        # for i in high_lst:
        #     if index < 10:
        #         print(i)
        #         index += 1

        # if not group_by_name:###Zdes ya ne ponimau kak rabotaet True False i chto nado sdelat

        # else:

            # for i in range(len(high_lst) - 1):  ##Sortiruem puzrkom/ Seichas puzirek uzhe ne nuzhen
            #     index_1 = 0
            #     for j in range(len(high_lst) - i - 1):
            #         if high_lst[index_1] > high_lst[index_1 + 1]:
            #             high_lst[index_1], high_lst[index_1 + 1] = high_lst[index_1 + 1], high_lst[index_1]
            #             index_1 += 1
            #         elif high_lst[index_1] < high_lst[index_1 + 1]:
            #             index_1 += 1

                # with open('output.csv', "w") as f:
                #     writer = csv.writer(f)
                #     writer.writerow(group_by_name)
            #
            # if order == 'asc': ##Zanosim v cvs file po vozrastaniu
            #     with open('output.csv', "w") as f:
            #         writer = csv.writer(f)
            #         writer.writerow(high_lst)
            #
            # else:## ##Zanosim v cvs file po ubivaniu
            #     high_lst_revers = reversed(high_lst)
            #     with open('output.csv', "w") as f:
            #         writer = csv.writer(f)
            #         writer.writerow(list(high_lst_revers))

##############U nas est spisok, teper nado svormirovat slovar i otsortirovat ego po etomu spisku



def poisk(limit=10):###Ishem PCLN 2017-08-08(takogo znacheniya net)####'2013-02-12'
    global srez
    name = []
    get_columns = itemgetter('date', 'open', 'high', 'low', 'close', 'volume', 'Name')
    with open('output_sorted_PCLN') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name.append(row['Name'])##Poluchaem spisok name, po nemu budem potom sortirovat(obrashatsya)
            # print(len(name))
    mass = {}
    index = 0
    for i in name:
        if index < 5:
            print(i)
            index += 1
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
    # print(index)
    # print(len(mass))

            ##Nuzno mass sdelat polnim 619040, a ne 440062
    with open('output_sorted_PCLN') as csvfile:  ##Sortiruem po imeni PCLN Len obshii 619040
        reader = csv.DictReader(csvfile)
        index_1 = 0
        # name = [str(x) for x in name]## Sozdali spisok 619040 elementov
        counter = 0
        for row in islice(reader, 619040):  #
            mass[index_1] = get_columns(row)  ##V
            index_1 += 1
        # print(len(mass))##619040

    def find_f(mass, index):  ##Funkciu s longreada vzyal
        ##Nahodim kolichestvo povtoriaushihsa imen znaya, chto pervii element na 440062 meste
        ###'PCLN': 1259
        freq = {}  # словарь для хранения частоты каждого элемента в списке

        # пространство поиска nums[left…right]
        # print(index)
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
    # print(freq)
    for k in freq:
        if k == 'PCLN':
            srez = int(freq[k])
            # print(srez)#1259 kolichestvo odinakovih tikerov
            # print(mass[440063]) #index s kot nachinautsya
            # print(index)#on zhe
            # print(len(mass))
    sort_PCLN = {}#Zapishem v slovar 1259 znachenii PCLN

    index_1=0

    for k in range(len(mass)):
        if index >= index_1:
            index_1 += 1
        if index < index_1 and len(sort_PCLN)<srez:
            sort_PCLN[k] = mass[index_1]

            #keys = sort_PCLN[0]
    print(len(sort_PCLN)) #1259
    print(sort_PCLN[440063])#('2013-02-12', '696.8', '705.77', '695.37', '703.38', '487096', 'PCLN')
    # index=0
    # for i in sort_PCLN:
    #     if index < 5:
    #         print(i)
    #         index += 1
# 440062 Indexi PCLN
# 440063
# 440064
# 440065
# 440066
    f = []
    index_1 = 0
    for i in sort_PCLN:
        if sort_PCLN[i][0] == '2013-02-12':
            f.append(sort_PCLN[i])
            break
    print(f)###f vivodit znachenie PCLN na '2013-02-12'

        # with open('out_PCLN.cvs', "w", newline='') as f:
        #     dict_writer = csv.DictWriter(f, keys)
        #     dict_writer.writeheader()
        #     dict_writer.writerow(sort_PCLN)  ###Pishet tolko 1 strochku, bolshego dobitsia  ne smog
poisk()