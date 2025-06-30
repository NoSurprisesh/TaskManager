import json
import os
from task import Task
from user import User

def save_task(task: Task, current_user: User ) -> None:
    file_path = current_user.get_task_file()
    full_path = f'data/{file_path}'

    if not os.path.exists('data'):
        os.makedirs('data')

    tasks = load_tasks(current_user)
    tasks.append(task)

    with open(full_path, 'w', encoding='utf-8') as file:
        json.dump([t.to_dict() for t in tasks], file, indent=4, ensure_ascii=False)

def load_tasks(current_user: User) -> list[Task]:
    file_path = current_user.get_task_file()
    full_path = f'data/{file_path}'

    if not os.path.exists(full_path):
        return []

    with open(full_path, 'r', encoding='utf-8') as file:
        try:
            tasks_data = json.load(file)
            return [Task.from_dict(task) for task in tasks_data]
        except json.JSONDecodeError:
            return []


def save_all_tasks(tasks: list[Task], current_user: User) -> None:
    if not os.path.exists('data'):
        os.makedirs('data')
    file_path = current_user.get_task_file()
    full_path = f'data/{file_path}'
    with open(full_path, 'w', encoding='utf-8') as file:
        json.dump([t.to_dict() for t in tasks], file, indent=4, ensure_ascii=False)

