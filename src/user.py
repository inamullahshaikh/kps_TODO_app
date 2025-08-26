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
        return self._password

    def change_password(self,old_pass, new_pass):
        if old_pass == self._password:
            self._password = new_pass
    def add_comment(self, comment):
        self._comments.append(comment)
    def remove_comment(self, comment):
        self._comments.remove(comment)
    def get_comments(self):
        return self._comments
    def add_namespace(self, namespace):
        self._namespaces.append(namespace)
    def remove_namespace(self, namespace):
        self._namespaces.remove(namespace)
    def get_namespaces(self):
        return self._namespaces
    def add_task(self, task):
        self._tasks.append(task)
    def remove_task(self, task):
        self._tasks.remove(task)
    def login(self, username, password):
        if self._username == username and self._password == password:
            self._logged_in = True
            return True
        return False

    def logout(self):
        if self._logged_in:
            self._logged_in = False
        else:
            print("You are not logged in.")
    def __str__(self):
        namespaces_list = ", ".join([str(ns) for ns in self._namespaces]) if self._namespaces else "None"
        return (
            f"User: {self._username}\n"
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Email: {self.email}\n"
            f"Phone number: {self.phone}\n"
            f"Namespaces: {len(self._namespaces)}\n{namespaces_list}\n"
            f"Comments: {len(self._comments)}\n{self._comments}\n"
            f"Tasks Assigned: {len(self._tasks)}\n{self._tasks}\n"
        )

    def __repr__(self):
        return f"User: {self._username}\nName: {self.name}\nAge: {self.age}\nEmail: {self.email}\nPhone number: {self.phone}\nPassword: {self.password}\n"
