import json
import os
from task import Task


def save_task(task: Task, file_path = 'tasks.json') -> None:
    if not os.path.exists('data'):
        os.makedirs('data')
    with open(f'data/{file_path}', 'w') as file:
        json.dump(task.to_dict(), file, indent=4)

def load_tasks(file_path = 'tasks.json') -> list[Task]:
    if not os.path.exists(f'data/{file_path}'):
        print('tasks.json does not exist')
        return []
    with open(f'data/{file_path}', 'r') as file:
        tasks = json.load(file)
    data = []
    data.append(Task.from_dict(tasks))
    return data
