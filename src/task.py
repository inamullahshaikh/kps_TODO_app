from .status import Status  # Assuming Status class is in status.py
from .comment import Comment

class Task:
    PRIORITIES = ["Low", "Medium", "High"]
    ID = 100000

    def __init__(self, name, creator, project, due_date, description, status=None, priority="Medium"):
        self._name = name
        self._creator = creator
        self._project = project
        self._due_date = due_date
        self._description = description
        self._users = []
        self._comments = []  # List of Comment objects
        self._id = Task.ID
        Task.ID += 1
        self._status = Status(status) if status else Status()
        self._priority = priority if priority in Task.PRIORITIES else "Medium"

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        if value in Task.PRIORITIES:
            self._priority = value

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, value):
        self._creator = value

    @property
    def project(self):
        return self._project

    @project.setter
    def project(self, value):
        self._project = value

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, value):
        self._due_date = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def users(self):
        return self._users.copy()

    def add_user(self, user):
        if user not in self._users:
            self._users.append(user)
            return True
        return False

    def remove_user(self, user):
        if user in self._users:
            self._users.remove(user)
            return True
        return False

    @property
    def status(self):
        return self._status.status

    def update_status(self, new_status):
        self._status.update_status(new_status)

    @property
    def comments(self):
        return self._comments.copy()

    def add_comment(self, user, text):
        new_comment = Comment(user, self, text)
        self._comments.append(new_comment)
        return new_comment

    def remove_comment(self, comment):
        if comment in self._comments:
            self._comments.remove(comment)
            return True
        return False

    def list_comments(self):
        if not self._comments:
            return "No comments yet."
        return "\n".join([f"- {c.user.username}: {c.text}" for c in self._comments])

    # --- String Representation ---
    def __str__(self):
        users_list = ", ".join([user.username for user in self._users]) if self._users else "None"
        return (
            f"Task ID: {self._id}\n"
            f"Name: {self._name}\n"
            f"Creator: {self.creator.username}\n"
            f"Project: {self._project.name}\n"
            f"Due Date: {self._due_date}\n"
            f"Description: {self._description}\n"
            f"Status: {self._status.status}\n"
            f"Priority: {self._priority}\n"
            f"Assigned Users: {users_list}\n"
            f"Comments:\n{self.list_comments()}"
        )

    def __repr__(self):
        return (
            f"<Task(id={self._id}, name='{self._name}', project='{self._project}', "
            f"due_date='{self._due_date}', status='{self._status.status}', users={len(self._users)}, comments={len(self._comments)})>"
        )
