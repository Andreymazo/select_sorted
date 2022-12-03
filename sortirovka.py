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
    #####Сначала пробежим и найдем наибольший элемент
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
                if counter == 0:  ##Услловие выхода из прогграммы, весь список отсортирован
                    result = True
                    break

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
        high = keys[:] + values[:]
    print(high, ost)

    # result = True #почемуто и без result = True останавливается

    return result


result = f_3(high, ost, result)
