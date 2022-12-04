def f_1(high):## Uberem duplicati ostavim unicalnie elemeni, no ne poteriyaem ih a slo;bv v ost
    ost = []
    for x in high:
        if high.count(x) > 1:
            ost.append(x)
            high.remove(x)

    return high, ost
            # print(high, ost)


high, ost = f_1([1, 3, 11, 7, 9, 2, 4, 8, 1, 6, 8])


def f_2(high, ost):###Минимальное число справа и проверка на отсортированность counter = 0
    # counter счетчик заменыб если нуль, то отсортирован
    #####Сначала пробежим и найдем наименьший элемент
    result = False
    while not result:#Сюда надо снова подать будет список после его сортировки пополам, т.е. high из функции f_3

        index = 0
        counter = 0
        for i in range(len(high)-1):
            try:
                if high[index] < high[index + 1]:
                    high[index], high[index + 1] = high[index + 1], high[index]  ###Наименьший элемент в конце цикла окажется на последнем месте
                    index += 1
                    counter += 1
                if high[index] > high[index + 1]:
                    index += 1
                if high[index] == high[index + 1]:
                    ost.append(high[index])  ##Дубликат заносим в ost
                    high.remove(high[index])  ##Дубликат убираем
                if counter == 0:  ##Услловие выхода из прогграммы, весь список отсортирован, ni odnogo izmenenia ne proizoshlo
                    print(counter, high, ost)
                    result = True## V etoi tochke dolzhen bit otsortirovannii spisok high i spisok ost s duplicarami
                    break#No pochemu to go konca nedosortirovivaet

            except IndexError:
                pass
            continue

    return high, ost, result


high, ost, result = f_2(high, ost)


def f_3(high, ost, result):##Делим список на 2 сравниваем соседние элементы и складываем обратно
        b = int(len(high) % 2)
        if b == True:
            ost = ost[:] + high[:b]  # ostatok ot delenia v massiv minimalnoe znachenie s poslednego mesta
            high = high[1:1] + high[1:] # убираем первый элементб если есть остаток 1
        y = int(len(high) / 2)  # длина половинки
        # print(high)
        p = high[:y]
        z = high[y:]
        x = dict(zip(z, p))
        new = {}
        counter = 0
        for k, v in x.items():
            if k > v:
                new.update({k: v})
            if k < v:
                new.update({v: k})
                counter += 1
            keys = [*new]  ##Razlozhenie slovaria na spiski
            values = [*new.values()]
            # print(keys, values)
            high = keys[:] + values[:] + ost[b:-b]#Vozvrashaem na mesto element b
            print(high, ost)


#Opredeliaem duplicati ix indexi zanosim v spisok mass
# high = [9, 8, 7, 4, 6, 3, 2, 1]
# ost = [1, 8, 11]
mass = []
for i in ost:
    if i in high:
        index_1 = 0
        for j in high:  # Nahodim index duplikata v high
            if j == i:
                mass.append(high[index_1])  ##Zanosim v mass znachenie i index
                mass.append(index_1)

            elif j != i:
                index_1 += 1

            print(high, mass, ost)
          ############ [11, 9, 8, 7, 4, 6, 3, 2, 1][1, 7, 8, 1][1, 8]
####Dobavliaem v high duplicati udaliaem iz ost i dobavlaem ostavshiesya


index_1 = 0
while index_1 <= int(len(mass))-1:
    for i in mass:
        high.insert(mass[index_1 + 1], mass[index_1])  ###Vidaet oshibku: IndexError: list index out of range
        if i in ost:
            ost.remove(i)
        index_1 += 2
        print(high, mass, ost)
    # try:
    # except IndexError:
    #     pass
    # continue


result = f_3(high, ost, result)
############################################################

# high = [9, 8, 7, 4, 6, 3, 2, 1]
# ost = [1, 8, 11]
# mass = []
#
# for i in range(len(ost)):
#     if i in high:
#         index_1 = 0
#         for j in high:  # Nahodim index duplikata v high
#             if j == i:
#                 mass.append(high[index_1])  ##Zanosim v mass znachenie i index
#                 mass.append(index_1)
#                 ost.remove(i)
#
#                 # high.insert(index_1, j)
#
#             elif j != i:
#                 index_1 += 1
#
#             print(high, mass, ost)
# ##################################
#             # , print(high, ost)
# # sets.union(*others) # new method
# # sets.symmetric_difference_update().