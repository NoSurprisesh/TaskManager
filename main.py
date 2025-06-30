from parser import parse_add_command
from storage import save_task, load_tasks

def main():
    while True:
        user_input = input('>>> ')

        if user_input.startswith('/add'):
            try:
                task = parse_add_command(user_input)
                save_task(task)
                print('Task saved!')
            except ValueError as e:
                print(f'Error: {e}')

        elif user_input.startswith('/show'):
            tasks = load_tasks()
            if not tasks:
                print('Tasks list is empty!')
            else:
                for task in sorted(tasks, key=lambda task: task.date):
                    print(f'[{task.date.strftime('%d.%m.%Y %H:%M')}] '
                          f'[{task.priority.upper()}] '
                          f'{task.title.capitalize()} '
                          f'[{task.description.capitalize()}]')

        elif user_input.startswith('/exit'):
            print('Goodbye!')
            break

        else:
            print('Unknown command!')

main()




