class Namespace:
    ID = 100000

    def __init__(self, name, creator):
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
        return self._projects

    @projects.setter
    def projects(self, value):
        if not isinstance(value, list):
            raise ValueError("Projects must be a list")
        self._projects = value

    @property
    def users(self):
        return self._users

    @users.setter
    def users(self, value):
        if not isinstance(value, list):
            raise ValueError("Users must be a list")
        self._users = value

    @property
    def id(self):
        return self._id

    def add_project(self, project):
        self._projects.append(project)

    def add_user(self, user):
        self._users.append(user)

    def remove_project(self, project):
        self._projects.remove(project)

    def remove_user(self, user):
        self._users.remove(user)

    def __str__(self):
        s = f"Namespace(ID: {self._id}, Name: {self._name}\nCreator:\n {self._creator.name}\nProjects: {len(self.projects)}\n"
        for pro in self.projects:
            s += f"{pro}"

        s += f"\nUsers: {len(self._users)}\n"
        for user in self._users:
            s += f"{user.username}"
        return s

    def __del__(self):
        print(f"Deleting Namespace '{self._name}' (ID: {self._id}) → Deleting all projects")
        self._projects.clear()
