import datetime
from .namespace import Namespace

class Project:
    ID = 100000

    def __init__(self, name, due_date, namespace: Namespace):
        self._name = name
        self._due_date = due_date
        self._project_id = Project.ID
        Project.ID += 1
        self._tasks = []
        self._namespace = namespace

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Project name must be a string")
        self._name = value

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, value):
        if not isinstance(value, datetime.date):
            raise ValueError("Not in date format(YYYY-MM-DD)")
        self._due_date = value

    @property
    def project_id(self):
        return self._project_id

    @property
    def tasks(self):
        return self._tasks

    @tasks.setter
    def tasks(self, value):
        if not isinstance(value, list):
            raise ValueError("Tasks must be a list")
        self._tasks = value

    @property
    def namespace(self):
        return self._namespace

    @namespace.setter
    def namespace(self, value):
        if not isinstance(value, Namespace):
            raise ValueError("Namespace must be an instance of Namespace class")
        self._namespace = value

    def add_task(self, task):
        self._tasks.append(task)
    def remove_task(self, task):
        self._tasks.remove(task)

    def __str__(self):
        s = f"Project ID: {self._project_id}, Name: {self._name}, Due Date: {self._due_date}\nNamespace: {self._namespace.name}\nTasks: {len(self._tasks)}"
        for task in self._tasks:
            s += f"\n{task}"
        s += "\n"
        return s

    def __del__(self):
        print(f"Deleting Project '{self._name}' (ID: {self._project_id}) → Clearing all tasks")
        self._tasks.clear()
