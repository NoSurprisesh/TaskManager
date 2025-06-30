from datetime import datetime


class Task:
    def __init__(self,
                 title : str,
                 date : datetime,
                 priority : str = 'medium',
                 status : str = 'new',
                 description : str = 'no description',):
        self.title = title
        self.date = date
        self.priority = priority
        self.status = status
        self.description = description

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "date": self.date.strftime('%d.%m.%Y %H:%M'),
            "priority": self.priority,
            "status": self.status,
            "description": self.description,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            title=data['title'],
            date=datetime.strptime(data['date'], '%d.%m.%Y  %H:%M'),
            priority=data['priority'],
            status=data['status'],
            description=data['description'],
        )