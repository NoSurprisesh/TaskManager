import shlex
from datetime import datetime
from parser import parse_add_command
from storage import save_task, load_tasks, save_all_tasks

def handle_input(user_input: str) -> None:
    if user_input.startswith("/add"):
        handle_add(user_input)
    elif user_input.startswith("/show"):
        handle_show()
    elif user_input.startswith("/delete"):
        handle_delete(user_input)
    elif user_input.startswith("/edit"):
        handle_edit(user_input)
    else:
        print("Unknown command!")

def handle_add(user_input):
    try:
        task = parse_add_command(user_input)
        save_task(task)
        print("Task saved!")
    except ValueError as e:
        print(f"Error: {e}")

def handle_show():
    tasks = load_tasks()
    if not tasks:
        print("Task list is empty!")
    else:
        for i, task in enumerate(sorted(tasks, key=lambda task: task.date), start=1):
            print(f"{i}. [{task.date.strftime('%d.%m.%Y %H:%M')}] "
                  f"[{task.priority.upper()}] "
                  f"{task.title.capitalize()} "
                  f"[{task.description.capitalize()}]")

def handle_delete(user_input):
    try:
        index = int(user_input.split()[1]) - 1
        tasks = sorted(load_tasks(), key=lambda t: t.date)
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_all_tasks(tasks)
            print(f"Removed: {removed.title}")
        else:
            print("Invalid task index.")
    except (IndexError, ValueError):
        print('Error: input "/delete <number>"')

def handle_edit(user_input):
    try:
        parts = user_input.split(maxsplit=2)
        index = int(parts[1]) - 1
        args = shlex.split(parts[2]) if len(parts) > 2 else []

        tasks = sorted(load_tasks(), key=lambda t: t.date)
        if 0 <= index < len(tasks):
            task = tasks[index]

            for i in range(len(args)):
                if args[i] == '--title':
                    task.title = args[i + 1]
                elif args[i] == '--date':
                    date_str = args[i + 1]
                elif args[i] == '--time':
                    time_str = args[i + 1]
                elif args[i] == '--priority':
                    task.priority = args[i + 1]
                elif args[i] == '--description':
                    task.description = args[i + 1]

            if 'date_str' in locals() and 'time_str' in locals():
                task.date = datetime.strptime(f'{date_str} {time_str}', '%d.%m.%Y %H:%M')

            save_all_tasks(tasks)
            print(f"Edited: {task.title}")
        else:
            print("Invalid task index.")
    except Exception as e:
        print(f"Editing error: {e}")