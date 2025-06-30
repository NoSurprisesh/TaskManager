class User:
    def __init__(self, username):
        self.username = username

    def get_task_file(self) -> str:
        return f"tasks_{self.username}.json"