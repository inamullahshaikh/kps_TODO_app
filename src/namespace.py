class Namespace:
    ID = 100000

    def __init__(self, name, creator):
        if not isinstance(name, str):
            raise ValueError("Namespace name must be a string")
        self._name = name
        self._creator = creator 
        self._projects = []
        self._users = []
        self._id = Namespace.ID
        Namespace.ID += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value

    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, value):
        self._creator = value 

    @property
    def projects(self):
        return self._projects.copy()

    @property
    def users(self):
        return self._users.copy()

    @property
    def id(self):
        return self._id

    def add_project(self, project):
        if project not in self._projects:
            self._projects.append(project)
            return True
        return False

    def add_user(self, user):
        if user not in self._users:
            self._users.append(user)
            return True
        return False

    def remove_project(self, project):
        if project in self._projects:
            self._projects.remove(project)
            return True
        return False

    def remove_user(self, user):
        if user in self._users:
            self._users.remove(user)
            return True
        return False

    def __str__(self):
        projects_info = "\n".join([f"- {proj.name}" for proj in self._projects]) if self._projects else "No projects"
        users_info = ", ".join([user.username for user in self._users]) if self._users else "No users"
        return (
            f"Namespace(ID: {self._id}, Name: {self._name})\n"
            f"Creator: {getattr(self._creator, 'username', str(self._creator))}\n"
            f"Projects ({len(self._projects)}):\n{projects_info}\n"
            f"Users ({len(self._users)}): {users_info}"
        )

    def __repr__(self):
        return (
            f"<Namespace(id={self._id}, name='{self._name}', creator='{getattr(self._creator, 'username', str(self._creator))}', "
            f"projects={len(self._projects)}, users={len(self._users)})>"
        )
