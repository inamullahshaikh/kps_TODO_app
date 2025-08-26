class Task:
    ID = 100000
    def __init__(self, name, creator, project, due_date, description):
        self._name = name
        self._creator = creator
        self._project = project
        self._due_date = due_date
        self._description = description
        self._users = []
        self._id = self.ID
        self.ID += 1

    #GETTERS SETTERS USING DECORATORS
    @property
    def name(self):
        return self._name
    @property
    def creator(self):
        return self._creator
    @property
    def project(self):
        return self._project
    @property
    def due_date(self):
        return self._due_date
    @property
    def description(self):
        return self._description
    @property
    def users(self):
        return self._users
    @name.setter
    def name(self, value):
        self._name = value
    @creator.setter
    def creator(self, value):
        self._creator = value
    @project.setter
    def project(self, value):
        self._project = value
    @due_date.setter
    def due_date(self, value):
        self._due_date = value
    @description.setter
    def description(self, value):
        self._description = value
    @users.setter
    def users(self, value):
        self._users = value

    def add_user(self, user):
        self._users.append(user)
    def remove_user(self, user):
        self._users.remove(user)
    def __str__(self):
        return (
            f"Task ID: {self._id}\n"
            f"Name: {self._name}\n"
            f"Creator:\n{self._creator}\n"
            f"Project: {self._project}\n"
            f"Due Date: {self._due_date}\n"
            f"Description: {self._description}\n"
            f"Assigned Users: {', '.join(str(user) for user in self._users) if self._users else 'None'}"
        )
