from certifi import where

from .comment import Comment
from .namespace import Namespace
from .person import Person
from .project import Project
from .task import Task
from .user import User


class App:
    def __init__(self):
        self._users = {}
        self._logged_in_user = None

    def Signup_user(self,name, age, email, phone_number, username, password):
        self._users[username] = User(name, age, email, phone_number, username, password)
    def Login(self, username, password):
        if self._users[username].login(username, password) is True:
            self._logged_in_user = username

    def view_user(self):
        if self._logged_in_user is not None:
            print(self._users[self._logged_in_user])
        else:
            print("User not logged in")

    def update_user(self):
        if self._logged_in_user is not None:
            print("===== UPDATE MENU =====")
            print("Select the field you want to update:")
            print("1. Name")
            print("2. Age")
            print("3. Email")
            print("4. Phone Number")
            print("5. Username")
            print("6. Password")
            print("0. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                new_name = input("Enter new name: ")
                self._users[self._logged_in_user].name(new_name)
                print("Name updated successfully!")

            elif choice == '2':
                new_age = input("Enter new age: ")
                if new_age.isdigit():
                    self._users[self._logged_in_user].age(int(new_age))
                    print("Age updated successfully!")
                else:
                    print("Invalid age input!")

            elif choice == '3':
                new_email = input("Enter new email: ")
                self._users[self._logged_in_user].email(new_email)
                print("Email updated successfully!")

            elif choice == '4':
                new_phone = input("Enter new phone number: ")
                self._users[self._logged_in_user].phone_number(new_phone)
                print("Phone number updated successfully!")

            elif choice == '5':
                new_username = input("Enter new username: ")
                self._users[self._logged_in_user].username(new_username)
                print("Username updated successfully!")

            elif choice == '6':
                old_pass = input("Enter old password: ")
                new_password = input("Enter new password: ")
                self._users[self._logged_in_user].change_password(old_pass, new_password)
                print("Password updated successfully!")

            elif choice == '0':
                print("Update cancelled.")

            else:
                print("Invalid choice!")
        else:
            print("No user is currently logged in.")

    def create_namespace(self):
        name = input("Enter name of namespace: ")
        self._users[self._logged_in_user].add_namespace(Namespace(name, self._users[self._logged_in_user]))
        print("Namespace created successfully!")

    def add_user_to_namespace(self):
        username = input("Enter username of user to add: ")
        user = self._users.get(username)
        if not user:
            print("User not found.")
            return

        namespaces = self._users[self._logged_in_user].get_namespaces()
        if not namespaces:
            print("No namespaces available.")
            return

        print("Available namespaces:")
        for ns in namespaces:
            print(f"ID: {ns.id}, Name: {ns.name}")

        namespace_id = input("Enter namespace ID to add user to: ")
        try:
            namespace_id = int(namespace_id)  # Only if IDs are integers
        except ValueError:
            print("Invalid namespace ID.")
            return

        n = next((ns for ns in namespaces if ns.id == namespace_id), None)
        if not n:
            print("Namespace not found.")
            return

        n.add_user(user)
        print(f"User '{username}' added to namespace '{n.name}'.")


