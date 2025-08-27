import datetime
from .namespace import Namespace

class Project:
    ID = 100000

    def __init__(self, name: str, due_date: datetime.date, namespace: Namespace):
        if not isinstance(name, str):
            raise ValueError("Project name must be a string")
        if not isinstance(due_date, (datetime.date, datetime.datetime)):
            raise ValueError("Due date must be a datetime.date or datetime.datetime object")
        if not isinstance(namespace, Namespace):
            raise ValueError("Namespace must be an instance of Namespace class")

        self._name = name
        self._due_date = due_date
        self._project_id = Project.ID
        Project.ID += 1
        self._tasks = []
        self._namespace = namespace

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Project name must be a string")
        self._name = value

    @property
    def due_date(self) -> datetime.date:
        return self._due_date

    @due_date.setter
    def due_date(self, value: datetime.date):
        if not isinstance(value, (datetime.date, datetime.datetime)):
            raise ValueError("Due date must be a datetime.date or datetime.datetime object")
        self._due_date = value

    @property
    def project_id(self) -> int:
        return self._project_id

    @property
    def tasks(self) -> list:
        return self._tasks.copy()  
    
    def add_task(self, task) -> bool:
        if task not in self._tasks:
            self._tasks.append(task)
            return True
        return False

    def remove_task(self, task) -> bool:
        if task in self._tasks:
            self._tasks.remove(task)
            return True
        return False

    @property
    def namespace(self) -> Namespace:
        return self._namespace

    @namespace.setter
    def namespace(self, value: Namespace):
        if not isinstance(value, Namespace):
            raise ValueError("Namespace must be an instance of Namespace class")
        self._namespace = value

    def __str__(self) -> str:
        tasks_list = "\n".join([str(task) for task in self._tasks]) if self._tasks else "No tasks assigned"
        return (
            f"Project ID: {self._project_id}\n"
            f"Name: {self._name}\n"
            f"Due Date: {self._due_date}\n"
            f"Namespace: {self._namespace.name}\n"
            f"Tasks ({len(self._tasks)}):\n{tasks_list}"
        )

    def __repr__(self):
        return (
            f"<Project(id={self._project_id}, name='{self._name}', due_date='{self._due_date}', "
            f"namespace='{self._namespace.name}', tasks={len(self._tasks)})>"
        )
