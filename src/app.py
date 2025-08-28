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

        task = Task(task_name, self._users[self._logged_in_user], proj, due_date, description)
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
        user.add_task(task)
        print(f"User '{username}' assigned to task '{task.name}'.")

    def add_comment_to_task(self):
        user = self._users[self._logged_in_user]
        tasks = user.get_tasks()
        if not tasks:
            print("You have no tasks assigned.")
            return

        print("\nYour Tasks:")
        for t in tasks:
            print(f"ID: {t.id}, Name: {t.name}, Status: {t.status}")

        try:
            task_id = int(input("\nEnter Task ID to add a comment: "))
        except ValueError:
            print("Invalid input. Please enter a numeric Task ID.")
            return
        task = next((t for t in tasks if t.id == task_id), None)
        if not task:
            print("Task not found.")
            return
        comment_text = input("Enter your comment: ").strip()
        if not comment_text:
            print("Comment cannot be empty.")
            return

        task.add_comment(user, comment_text)
        user.add_comment(Comment(user, task, comment_text))
        print(f"Comment added successfully: {comment_text}")

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

    def view_user_comments(self):
        user = self._users.get(self._logged_in_user)
        if not user:
            print("User not found.")
            return

        comments = user.get_comments()
        if not comments:
            print("No comments found.")
            return

        print("\n--- VIEW COMMENTS ---")
        print("1. All\n2. By Namespace\n3. By Project\n4. By Task")
        choice = input("Choose option: ")

        if choice == '1':
            for c in comments:
                print(c)
        elif choice in ['2', '3', '4']:
            keyword = input("Enter name to filter: ").strip()
            filtered = []
            for c in comments:
                if choice == '2':  # By Namespace
                    if hasattr(c.task.project,
                               "namespace") and keyword.lower() in c.task.project.namespace.name.lower():
                        filtered.append(c)
                elif choice == '3':  # By Project
                    if keyword.lower() in c.task.project.name.lower():
                        filtered.append(c)
                elif choice == '4':  # By Task
                    if keyword.lower() in c.task.name.lower():
                        filtered.append(c)

            if filtered:
                for c in filtered:
                    print(c)
            else:
                print("No matching comments found.")
        else:
            print("Invalid option.")

    def change_task_status(self):
        user = self._users.get(self._logged_in_user)
        if not user:
            print("User not found.")
            return

        tasks = user.get_tasks()
        if not tasks:
            print("You have no tasks assigned.")
            return

        print("\nYour Tasks:")
        for t in tasks:
            print(f"ID: {t.id}, Name: {t.name}, Current Status: {t.status}")

        try:
            task_id = int(input("\nEnter Task ID to change status: "))
        except ValueError:
            print("Invalid input. Please enter a numeric Task ID.")
            return

        task = next((t for t in tasks if t.id == task_id), None)
        if not task:
            print("Task not found.")
            return

        current_status = task.status
        if current_status == "To Do":
            task.update_status("In Progress")
        elif current_status == "In Progress":
            task.update_status("Completed")
        else:
            print("Task already completed.")
            return

        print(f"Task status updated to {task.status}.")

    def show_tasks(self):
        print("\n--- SHOW TASKS ---")
        print("1. By Namespace\n2. By Project\n3. Missed Tasks\n4. All Tasks")
        choice = input("Choose option: ")

        namespaces = self._users[self._logged_in_user].get_namespaces()
        tasks = []

        if choice == '1':
            ns_name = input("Enter namespace name: ")
            for ns in namespaces:
                if ns.name == ns_name:
                    for proj in ns.projects:
                        tasks.extend(proj.tasks)
        elif choice == '2':
            proj_name = input("Enter project name: ")
            for ns in namespaces:
                for proj in ns.projects:
                    if proj.name == proj_name:
                        tasks.extend(proj.tasks)
        elif choice == '3':
            today = datetime.date.today()
            for ns in namespaces:
                for proj in ns.projects:
                    for task in proj.tasks:
                        if task.due_date < today and task.status != "Completed":
                            tasks.append(task)
        elif choice == '4':
            tasks = self._users[self._logged_in_user].get_tasks()
            print(tasks)
        if not tasks:
            print("No tasks found.")
            return

        print("\nSort by: 1. Name 2. Due Date 3. Priority")
        sort_choice = input("Choose: ")
        if sort_choice == '1':
            tasks.sort(key=lambda t: t.name)
        elif sort_choice == '2':
            tasks.sort(key=lambda t: t.due_date)
        elif sort_choice == '3':
            priority_order = {"High": 1, "Medium": 2, "Low": 3}
            tasks.sort(key=lambda t: priority_order[t.priority])

        for t in tasks:
            print(t)

    def view_user_projects(self):
        namespaces = self._users[self._logged_in_user].get_namespaces()
        if not namespaces:
            print("No namespaces found.")
            return

        print("\n--- VIEW PROJECTS ---")
        print("1. All Projects\n2. By Namespace")
        choice = input("Choose option: ")

        if choice == '1':
            for ns in namespaces:
                for proj in ns.projects:
                    print(proj)
        elif choice == '2':
            ns_name = input("Enter namespace name: ")
            for ns in namespaces:
                if ns.name == ns_name:
                    for proj in ns.projects:
                        print(proj)

    def run(self):
        while True:
            print("\n===== WELCOME =====")
            print("1. Signup")
            print("2. Login")
            print("0. Exit")
            
            choice = input("Enter choice: ")
            
            if choice == '1':
                self.signup_user()
            elif choice == '2':
                if self.login():
                    self.main_menu()
            elif choice == '0':
                print("Exiting...")
                break
            else:
                print("Invalid choice!")

    def main_menu(self):
        while True:
            print("\n===== MAIN MENU =====")
            print("1. View User")
            print("2. Update User")
            print("3. Create Namespace")
            print("4. Add User to Namespace")
            print("5. Add Project to Namespace")
            print("6. Add Task to Project")
            print("7. Assign User to Task")
            print("8. Add Comment to Task")
            print("9. View Namespaces")
            print("10. View Projects")
            print("11. View User Comments")
            print("12. View User Projects")
            print("13. Change Task Status")
            print("14. Show Tasks")
            print("15. Logout")
            
            choice = input("Enter choice: ")
            
            if choice == '1':
                self.view_user()
            elif choice == '2':
                self.update_user()
            elif choice == '3':
                self.create_namespace()
            elif choice == '4':
                self.add_user_to_namespace()
            elif choice == '5':
                self.add_project_to_namespace()
            elif choice == '6':
                self.add_task_to_project()
            elif choice == '7':
                self.assign_user_to_task()
            elif choice == '8':
                self.add_comment_to_task()
            elif choice == '9':
                self.view_namespace()
            elif choice == '10':
                self.view_project()
            elif choice == '11':
                self.view_user_comments()
            elif choice == '12':
                self.view_user_projects()
            elif choice == '13':
                self.change_task_status()
            elif choice == '14':
                self.show_tasks()
            elif choice == '15':
                print("Logging out...")
                break
            else:
                print("Invalid choice!")
