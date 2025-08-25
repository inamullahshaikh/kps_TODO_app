class Namespace:
    def __init__(self, name, creator):
        self._name = name
        self._creator = creator
        self._projects = []
        self._users = []
    def __del__(self):
        for project in self._projects:
            project.delete()
    def add_project(self, project):
        self._projects.append(project)

    def remove_project(self, project):
        self._projects.remove(project)

    def get_projects(self):
        return self._projects
