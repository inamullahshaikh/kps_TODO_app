from .person import Person

class User(Person):
    def __init__(self, name, age, email, phone_number, username, password):
        super().__init__(name, age, email, phone_number)
        self._username = username
        self._password = password
        self._namespaces = []
        self._comments = []
        self._tasks = []
        self._logged_in = False

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def password(self):
        # For security reasons, do NOT expose real password
        return "********"

    def change_password(self, old_pass, new_pass):
        if old_pass == self._password:
            self._password = new_pass
            return True
        return False

    def add_comment(self, comment):
        self._comments.append(comment)
        return True

    def remove_comment(self, comment):
        if comment in self._comments:
            self._comments.remove(comment)
            return True
        return False

    def get_comments(self):
        return self._comments.copy()

    def add_namespace(self, namespace):
        self._namespaces.append(namespace)
        return True

    def remove_namespace(self, namespace):
        if namespace in self._namespaces:
            self._namespaces.remove(namespace)
            return True
        return False

    def get_namespaces(self):
        return self._namespaces.copy()

    def add_task(self, task):
        self._tasks.append(task)
        return True

    def remove_task(self, task):
        if task in self._tasks:
            self._tasks.remove(task)
            return True
        return False
    def get_tasks(self):
        return self._tasks.copy()
    def login(self, username, password):
        if self._logged_in:
            return "Already logged in."
        if self._username == username and self._password == password:
            self._logged_in = True
            return True
        return False

    def logout(self):
        if self._logged_in:
            self._logged_in = False
            return True
        return False

    def __str__(self):
        namespaces_list = ", ".join([str(ns) for ns in self._namespaces]) if self._namespaces else "None"
        comments_list = ", ".join([str(c) for c in self._comments]) if self._comments else "None"
        tasks_list = ", ".join([str(t) for t in self._tasks]) if self._tasks else "None"

        return (
            f"User: {self._username}\n"
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Email: {self.email}\n"
            f"Phone number: {self.phone}\n"
            f"Namespaces ({len(self._namespaces)}): {namespaces_list}\n"
            f"Comments ({len(self._comments)}): {comments_list}\n"
            f"Tasks Assigned ({len(self._tasks)}): {tasks_list}\n"
        )

    def __repr__(self):
        return (
            f"<User(username='{self._username}', name='{self.name}', "
            f"age={self.age}, email='{self.email}', phone='{self.phone_number}')>"
        )
