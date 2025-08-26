class Comment:
    def __init__(self, user, task, text):
        self._user = user
        self._task = task
        self._text = text

    @property
    def user(self):
        return self._user
    @property
    def task(self):
        return self._task
    @property
    def text(self):
        return self._text
    @user.setter
    def user(self, user):
        self._user = user
    @task.setter
    def task(self, task):
        self._task = task
    @text.setter
    def text(self, text):
        self._text = text

    def __str__(self):
        return f"{self.text}\nUser: {self.user}\nTask: {self.task}\n"