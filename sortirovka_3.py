

def f_2(high):###Минимальное число справа и проверка на отсортированность counter = 0
    # counter счетчик заменыб если нуль, то отсортирован
    #####Сначала пробежим и найдем наименьший элемент
    result = False
    while not result:#Сюда надо снова подать будет список после его сортировки пополам, т.е. high из функции f_3

        index = 0
        counter = 0
        for i in range(len(high)):
            try:
                #print(high)
                # if high[index] < high[index + 1] and index==len(high):
                #     index = 0
                if high[index] < high[index + 1]:
                    high[index], high[index + 1] = high[index + 1], high[index]  ###Наименьший элемент в конце цикла окажется на последнем месте
                    index += 1
                    counter += 1
                    print(counter, high)
                elif high[index] > high[index + 1]:
                    index += 1
                # if high[index] == high[index + 1]:
                #     ost.append(high[index])  ##Дубликат заносим в ost
                #     high.remove(high[index])  ##Дубликат убираем
                #     index += 1
                #     counter += 1
                    if counter == 0 and index == len(high)-1:  ##Услловие выхода из прогграммы, весь список отсортирован, ni odnogo izmenenia ne proizoshlo
                        print(counter, high)
                        result = True## V etoi tochke dolzhen bit otsortirovannii spisok high i spisok ost s duplicarami
                        break#No pochemu to go konca nedosortirovivaet

            except IndexError:
                pass
            continue

    return high, result


high, g = f_2([1, 3, 11, 7, 9, 2, 4, 8, 6])

