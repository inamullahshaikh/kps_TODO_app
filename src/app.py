from .comment import Comment
from .namespace import Namespace
from .person import Person
from .project import Project
from .task import Task
from .user import User
import datetime
import re

def validate_non_empty(prompt):
    value = input(prompt).strip()
    while not value:
        print("Input cannot be empty!")
        value = input(prompt).strip()
    return value

def validate_int(prompt, min_val=None, max_val=None):
    while True:
        value = input(prompt)
        if value.isdigit():
            value = int(value)
            if (min_val is None or value >= min_val) and (max_val is None or value <= max_val):
                return value
        print(f"Please enter a valid number between {min_val} and {max_val}.")

def validate_email(prompt):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    while True:
        email = input(prompt).strip()
        if re.match(pattern, email):
            return email
        print("Invalid email format!")

def validate_phone(prompt):
    pattern = r'^\+\d{10,15}$'
    while True:
        phone = input(prompt).strip()
        if re.match(pattern, phone):
            return phone
        print("Phone number must be in format +923001234567")

def validate_date(prompt):
    while True:
        date_str = input(prompt).strip()
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format! Use YYYY-MM-DD.")


class App:
    def __init__(self):
        self._users = {}
        self._logged_in_user = None
    def signup_user(self):
        print("\n--- SIGNUP ---")
        name = validate_non_empty("Enter name: ")
        age = validate_int("Enter age: ", 10, 120)
        email = validate_email("Enter email: ")
        phone_number = validate_phone("Enter phone number (e.g., +923001234567): ")
        
        while True:
            username = validate_non_empty("Choose username: ")
            if username in self._users:
                print("Username already exists! Try another.")
            else:
                break
        
        password = validate_non_empty("Choose password: ")

        self._users[username] = User(name, age, email, phone_number, username, password)
        print("User registered successfully!")


    def login(self):
        print("\n--- LOGIN ---")
        username = input("Enter username: ")
        password = input("Enter password: ")

        user = self._users.get(username)
        if not user:
            print("User not found!")
            return False

        if user.login(username, password):
            self._logged_in_user = username
            print(f"Welcome {username}!")
            return True
        else:
            print("Invalid credentials!")
            return False

    def logout(self):
        if self._logged_in_user:
            self._users[self._logged_in_user].logout()
            print(f"User {self._logged_in_user} logged out.")
            self._logged_in_user = None
        else:
            print("No user is logged in.")

    def view_user(self):
        if self._logged_in_user:
            print(self._users[self._logged_in_user])
        else:
            print("No user is logged in.")

    def update_user(self):
        if self._logged_in_user is None:
            print("No user is logged in.")
            return

        print("\n--- UPDATE USER ---")
        print("1. Name\n2. Age\n3. Email\n4. Phone Number\n5. Username\n6. Password\n0. Exit")
        choice = input("Enter choice: ")

        user = self._users[self._logged_in_user]

        if choice == '1':
            new_name = input("Enter new name: ")
            user.name = new_name
        elif choice == '2':
            new_age = input("Enter new age: ")
            if new_age.isdigit():
                user.age = int(new_age)
        elif choice == '3':
            user.email = input("Enter new email: ")
        elif choice == '4':
            user.phone_number = input("Enter new phone number: ")
        elif choice == '5':
            new_username = input("Enter new username: ")
            self._users[new_username] = self._users.pop(self._logged_in_user)
            self._logged_in_user = new_username
        elif choice == '6':
            old_pass = input("Enter old password: ")
            new_pass = input("Enter new password: ")
            if user.change_password(old_pass, new_pass):
                print("Password updated.")
            else:
                print("Incorrect old password!")
        elif choice == '0':
            return
        else:
            print("Invalid choice!")

    def create_namespace(self):
        if self._logged_in_user is None:
            print("Login first!")
            return

        name = input("Enter namespace name: ")
        namespace = Namespace(name, self._users[self._logged_in_user])
        self._users[self._logged_in_user].add_namespace(namespace)
        print(f"Namespace '{name}' created!")

    def add_user_to_namespace(self):
        if self._logged_in_user is None:
            print("Login first!")
            return

        username = input("Enter username to add: ")
        user = self._users.get(username)
        if not user:
            print("User not found.")
            return

        namespaces = self._users[self._logged_in_user].get_namespaces()
        if not namespaces:
            print("No namespaces available.")
            return

        print("Namespaces:")
        for ns in namespaces:
            print(f"ID: {ns.id}, Name: {ns.name}")

        ns_id = int(input("Enter namespace ID: "))
        ns = next((n for n in namespaces if n.id == ns_id), None)
        if ns:
            ns.add_user(user)
            print(f"User '{username}' added to '{ns.name}'.")
        else:
            print("Invalid namespace ID.")

    def add_project_to_namespace(self):
        namespaces = self._users[self._logged_in_user].get_namespaces()
        if not namespaces:
            print("You have no namespaces.")
            return

        print("Namespaces:")
        for ns in namespaces:
            print(f"ID: {ns.id}, Name: {ns.name}")

        ns_id = validate_int("Enter namespace ID: ")
        ns = next((n for n in namespaces if n.id == ns_id), None)
        if not ns:
            print("Namespace not found.")
            return

        project_name = validate_non_empty("Enter project name: ")
        due_date = validate_date("Enter due date (YYYY-MM-DD): ")

        project = Project(project_name, due_date, ns)
        ns.add_project(project)
        print(f"Project '{project_name}' added to namespace '{ns.name}'.")

    def add_task_to_project(self):
        namespaces = self._users[self._logged_in_user].get_namespaces()
        if not namespaces:
            print("You have no namespaces.")
            return

        print("Namespaces:")
        for ns in namespaces:
            print(f"ID: {ns.id}, Name: {ns.name}")

        ns_id = int(input("Enter namespace ID: "))
        ns = next((n for n in namespaces if n.id == ns_id), None)
        if not ns:
            print("Namespace not found.")
            return

        if not ns.projects:
            print("No projects in this namespace.")
            return

        print("Projects:")
        for proj in ns.projects:
            print(f"ID: {proj.project_id}, Name: {proj.name}")

        proj_id = int(input("Enter project ID: "))
        proj = next((p for p in ns.projects if p.project_id == proj_id), None)
        if not proj:
            print("Project not found.")
            return

        task_name = input("Enter task name: ")
        description = input("Enter description: ")
        due_date_str = input("Enter task due date (YYYY-MM-DD): ")
        try:
            due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format!")
            return

        task = Task(task_name, self._users[self._logged_in_user], proj.name, due_date, description)
        proj.add_task(task)
        print(f"Task '{task_name}' added to project '{proj.name}'.")

    def assign_user_to_task(self):
        namespaces = self._users[self._logged_in_user].get_namespaces()
        if not namespaces:
            print("You have no namespaces.")
            return

        print("Namespaces:")
        for ns in namespaces:
            print(f"ID: {ns.id}, Name: {ns.name}")

        ns_id = int(input("Enter namespace ID: "))
        ns = next((n for n in namespaces if n.id == ns_id), None)
        if not ns:
            print("Namespace not found.")
            return

        if not ns.projects:
            print("No projects in this namespace.")
            return

        print("Projects:")
        for proj in ns.projects:
            print(f"ID: {proj.project_id}, Name: {proj.name}")

        proj_id = int(input("Enter project ID: "))
        proj = next((p for p in ns.projects if p.project_id == proj_id), None)
        if not proj:
            print("Project not found.")
            return

        if not proj.tasks:
            print("No tasks in this project.")
            return

        print("Tasks:")
        for t in proj.tasks:
            print(f"Name: {t.name}, ID: {t.id}")

        task_id = int(input("Enter Task ID: "))
        task = next((t for t in proj.tasks if t.id == task_id), None)
        if not task:
            print("Task not found.")
            return

        print("Users in namespace:")
        for user in ns.users:
            print(user.username)

        username = input("Enter username to assign: ")
        user = next((u for u in ns.users if u.username == username), None)
        if not user:
            print("User not in namespace.")
            return

        task.add_user(user)
        print(f"User '{username}' assigned to task '{task.name}'.")

    def add_comment_to_task(self):
        namespaces = self._users[self._logged_in_user].get_namespaces()
        if not namespaces:
            print("You have no namespaces.")
            return

        print("Namespaces:")
        for ns in namespaces:
            print(f"ID: {ns.id}, Name: {ns.name}")

        ns_id = int(input("Enter namespace ID: "))
        ns = next((n for n in namespaces if n.id == ns_id), None)
        if not ns:
            print("Namespace not found.")
            return

        if not ns.projects:
            print("No projects in this namespace.")
            return

        print("Projects:")
        for proj in ns.projects:
            print(f"ID: {proj.project_id}, Name: {proj.name}")

        proj_id = int(input("Enter project ID: "))
        proj = next((p for p in ns.projects if p.project_id == proj_id), None)
        if not proj:
            print("Project not found.")
            return

        if not proj.tasks:
            print("No tasks in this project.")
            return

        print("Tasks:")
        for t in proj.tasks:
            print(f"Name: {t.name}, ID: {t.id}")

        task_id = int(input("Enter Task ID: "))
        task = next((t for t in proj.tasks if t.id == task_id), None)
        if not task:
            print("Task not found.")
            return

        if self._users[self._logged_in_user] not in task.users:
            print("You are not assigned to this task.")
            return

        comment_text = input("Enter your comment: ")
        comment = Comment(self._users[self._logged_in_user], task, comment_text)
        self._users[self._logged_in_user].add_comment(comment)
        print("Comment added successfully!")

    def view_namespace(self):
        namespaces = self._users[self._logged_in_user].get_namespaces()
        if not namespaces:
            print("You have no namespaces.")
            return

        print("Namespaces:")
        for ns in namespaces:
            print(ns)

    def view_project(self):
        namespaces = self._users[self._logged_in_user].get_namespaces()
        if not namespaces:
            print("You have no namespaces.")
            return

        print("Namespaces:")
        for ns in namespaces:
            print(f"ID: {ns.id}, Name: {ns.name}")

        ns_id = int(input("Enter namespace ID: "))
        ns = next((n for n in namespaces if n.id == ns_id), None)
        if not ns:
            print("Namespace not found.")
            return

        if not ns.projects:
            print("No projects in this namespace.")
            return

        for proj in ns.projects:
            print(proj)

    def run(self):
        while True:
            print("\n===== MENU =====")
            print("1. Signup\n2. Login\n3. View User\n4. Update User\n5. Create Namespace\n6. Add User to Namespace\n"
                  "7. Add Project to Namespace\n8. Add Task to Project\n9. Assign User to Task\n10. Add Comment to Task\n"
                  "11. View Namespaces\n12. View Projects\n13. Logout\n0. Exit")

            choice = input("Enter choice: ")

            if choice == '1':
                self.signup_user()
            elif choice == '2':
                self.login()
            elif choice == '3':
                self.view_user()
            elif choice == '4':
                self.update_user()
            elif choice == '5':
                self.create_namespace()
            elif choice == '6':
                self.add_user_to_namespace()
            elif choice == '7':
                self.add_project_to_namespace()
            elif choice == '8':
                self.add_task_to_project()
            elif choice == '9':
                self.assign_user_to_task()
            elif choice == '10':
                self.add_comment_to_task()
            elif choice == '11':
                self.view_namespace()
            elif choice == '12':
                self.view_project()
            elif choice == '13':
                self.logout()
            elif choice == '0':
                print("Exiting...")
                break
            else:
                print("Invalid choice!")
