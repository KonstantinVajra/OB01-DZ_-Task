from datetime import datetime


class Task:
    def __init__(self, description: str, deadline: str):
        """
        Инициализация новой задачи

        Args:
            description: Описание задачи
            deadline: Срок выполнения в формате 'DD.MM.YYYY'
        """
        self.description = description
        self.deadline = datetime.strptime(deadline, '%d.%m.%Y')
        self.completed = False


class TaskManager:
    def __init__(self):
        """Инициализация менеджера задач"""
        self.tasks = []

    def add_task(self, description: str, deadline: str) -> None:
        """
        Добавление новой задачи

        Args:
            description: Описание задачи
            deadline: Срок выполнения в формате 'DD.MM.YYYY'
        """
        task = Task(description, deadline)
        self.tasks.append(task)
        print(f"Задача '{description}' добавлена")

    def mark_completed(self, index: int) -> None:
        """
        Отметить задачу как выполненную

        Args:
            index: Индекс задачи в списке (начиная с 1)
        """
        if 1 <= index <= len(self.tasks):
            task = self.tasks[index - 1]
            task.completed = True
            print(f"Задача '{task.description}' отмечена как выполненная")
        else:
            print("Неверный индекс задачи")

    def show_active_tasks(self) -> None:
        """Вывести список текущих (невыполненных) задач"""
        active_tasks = [task for task in self.tasks if not task.completed]

        if not active_tasks:
            print("Нет активных задач")
            return

        print("\nСписок текущих задач:")
        for i, task in enumerate(active_tasks, 1):
            deadline_str = task.deadline.strftime('%d.%m.%Y')
            print(f"{i}. {task.description} (срок: {deadline_str})")