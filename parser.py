import shlex
from datetime import datetime
from task import Task


def parse_add_command(command: str) -> Task:
    args = shlex.split(command)

    if not args or args[0] != '/add':
        raise ValueError('Invalid command')

    try:
        title = args[1]
        date = None
        time = None
        priority = 'medium'
        description = 'No description'

        for i in range(2, len(args)):
            if args[i] == '--date':
                date = args[i + 1]
            elif args[i] == '--time':
                time = args[i + 1]
            elif args[i] == '--priority':
                priority = args[i + 1]

        if not (title and date and time):
            raise ValueError('Required arguments not provided (title, date, time)')

        dt = datetime.strptime(f'{date} {time}', '%d.%m.%Y %H:%M')
        return Task(title=title, date=dt, priority=priority, description=description)

    except Exception as e:
        raise ValueError(f'Error of command parsing: {e}')