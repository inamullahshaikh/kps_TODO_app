from person import Person

class User(Person):
    def __init__(self, name, age, email, phone_number, username, password):
        super().__init__(name, age, email, phone_number)
        self._username = username
        self._password = password
        self._namespaces = []
        self._comments = []

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
    def __str__(self):
        return f"User: {self._username}\nName: {self.name}\nAge: {self.age}\nEmail: {self.email}\nPhone number: {self.phone}\n"
    def __repr__(self):
        return f"User: {self._username}\nName: {self.name}\nAge: {self.age}\nEmail: {self.email}\nPhone number: {self.phone}\nPassword: {self.password}\n"
