class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        self.completed = True

def add_task(tasks, description, due_date):
    tasks.append(Task(description, due_date))

def show_pending_tasks(tasks):
    print("Текущие задачи:")
    for i, task in enumerate(tasks, 1):
        if not task.completed:
            print(f"{i}. {task.description} (Срок: {task.due_date})")

def mark_task_completed(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index].mark_completed()
    else:
        print("Некорректный индекс задачи.")

tasks = []
add_task(tasks,"Выучить урок", "09.11.24")
add_task(tasks,"Открыть новый урок", "10.11.24")

show_pending_tasks(tasks)

mark_task_completed(tasks, 0)

show_pending_tasks(tasks)




