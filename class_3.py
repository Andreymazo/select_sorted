class Todo_list():

    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
        return task
    # def __str__(self):
    #      return str(self.tasks)


todo_list = Todo_list()

todo_list.add_task = ('Купить лампочку')
print(todo_list.__dict__)
# print(Todo_list.__dict__)
print(todo_list.tasks)
print("\n".join(todo_list.tasks))

# Поменять лампочку
# Выкинуть лампочку
