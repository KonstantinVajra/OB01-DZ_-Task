class Task:
    def __init__(self, description, due_date):
        """Инициализирует задачу с описанием, сроком выполнения и статусом невыполненной."""
        self.description = description
        self.due_date = due_date
        self.is_completed = False

    def mark_completed(self):
        """Отмечает задачу как выполненную."""
        self.is_completed = True

    def __str__(self):
        """Возвращает строковое представление задачи."""
        status = 'Выполнено' if self.is_completed else 'Не выполнено'
        return f"Задача: {self.description} | Срок: {self.due_date} | Статус: {status}"


class TaskManager:
    def __init__(self):
        """Инициализирует менеджер задач с пустым списком задач."""
        self.tasks = []

    def add_task(self, description, due_date):
        """Добавляет новую задачу."""
        task = Task(description, due_date)
        self.tasks.append(task)

    def mark_task_completed(self, index):
        """Отмечает задачу по индексу как выполненную."""
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
        else:
            print("Некорректный индекс задачи.")

    def show_pending_tasks(self):
        """Выводит список текущих (не выполненных) задач."""
        print("Текущие задачи:")
        pending_tasks = [task for task in self.tasks if not task.is_completed]
        if not pending_tasks:
            print("Нет текущих задач.")
        else:
            for i, task in enumerate(pending_tasks, 1):
                print(f"{i}. {task}")


# Пример использования
if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Купить продукты", "2024-11-10")
    manager.add_task("Закончить проект", "2024-11-15")

    print("До отметки задачи как выполненной:")
    manager.show_pending_tasks()

    manager.mark_task_completed(0)

    print("\nПосле отметки задачи как выполненной:")
    manager.show_pending_tasks()
