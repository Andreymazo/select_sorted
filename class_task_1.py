from _datetime import datetime as dt
#Для получения текущей даты и времени можно использвоать datetime.datetime.now()
class Task:

    def __init__(self, content):
        self.__content = content

    def __setitem__(self, key, value):
        print('Setitem exists')
        self.__content[key] = value
    def __getitem__(self, item):
        print('getitem exist')
        return self.__content[item], dt.now == self.__content
    def __keys(self):
        return (self.__content)

    def __eq__(self, other):
        if isinstance(other, Task):
            return self.__keys() == other.__keys()  # Sravnivaem dve stringi model,color dvuh ekzempliarov classa Cars
        return NotImplemented

    def __hash__(self):
        return hash(self.__keys())

    def __str__(self):
        return f'({self.__content}) создано {dt.now()}'
todo_list = set()
todo_list.add(Task('Сделать домашку'))
todo_list.add(Task('Выпить кофе'))
todo_list.add(Task('Выйти на пробежку'))
todo_list.add(Task('Сделать домашку'))

for item in todo_list:
    print(item)
    # >> > Task('Сделать домашку')
    # Сделать
    # домашку(создано
    # 2022 - 12 - 0
    # 8
    # 12: 05:16)
        # Сделать
        # домашку(создано
        # 2022 - 12 - 08
        # 12: 0
        # 9: 14)
        # Выпить
        # кофе(создано
        # 2022 - 12 - 0
        # 8
        # 12: 0
        # 9: 14)
        # Выйти
        # на
        # пробежку(создано
        # 2022 - 12 - 0
        # 8
        # 12: 0
        # 9: 14)























