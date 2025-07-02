from datetime import timedelta
from storage import load_tasks
from google_api import get_calendar_service

def sync_task_to_google(user):
    service = get_calendar_service(user.username)
    tasks = load_tasks(user)
    for task in tasks:
        event = {
            'summary': task.title,
            'description': task.description,
            'start': {
                'dateTime': task.date.isoformat(),
                'timeZone': 'Europe/Warsaw',
            },
            'end': {
                'dateTime': (task.date + timedelta(hours=1)).isoformat(),
                'timeZone': 'Europe/Warsaw',
            },
        }
        service.events().insert(calendarId='primary', body=event).execute()

    print(f'Synced {len(tasks)} tasks to Google Calendar.')