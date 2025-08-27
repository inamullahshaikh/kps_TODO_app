class Task:
    ID = 100000

    def __init__(self, name, creator, project, due_date, description):
        self._name = name
        self._creator = creator
        self._project = project
        self._due_date = due_date
        self._description = description
        self._users = []
        self._id = Task.ID
        Task.ID += 1      

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

    def __str__(self):
        users_list = ", ".join([getattr(user, 'username', str(user)) for user in self._users]) if self._users else "None"
        return (
            f"Task ID: {self._id}\n"
            f"Name: {self._name}\n"
            f"Creator: {getattr(self._creator, 'username', str(self._creator))}\n"
            f"Project: {self._project}\n"
            f"Due Date: {self._due_date}\n"
            f"Description: {self._description}\n"
            f"Assigned Users: {users_list}"
        )

    def __repr__(self):
        return (
            f"<Task(id={self._id}, name='{self._name}', project='{self._project}', "
            f"due_date='{self._due_date}', users={len(self._users)})>"
        )
