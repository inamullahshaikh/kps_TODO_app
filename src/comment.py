class Comment:
    def __init__(self, user, task, text: str):
        # Expect user and task to be objects from User and Task classes
        self._user = user
        self._task = task
        self._text = text

    # --- Properties ---
    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        self._user = user  # Could validate: isinstance(user, User)

    @property
    def task(self):
        return self._task

    @task.setter
    def task(self, task):
        self._task = task  # Could validate: isinstance(task, Task)

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        if not isinstance(text, str):
            raise ValueError("Comment text must be a string")
        self._text = text

    def __str__(self):
        username = getattr(self._user, 'username', str(self._user))
        task_name = getattr(self._task, 'name', str(self._task))
        return f"Comment: {self._text}\nUser: {username}\nTask: {task_name}"

    def __repr__(self):
        username = getattr(self._user, 'username', str(self._user))
        task_name = getattr(self._task, 'name', str(self._task))
        return f"<Comment(user='{username}', task='{task_name}', text='{self._text[:20]}...')>"
