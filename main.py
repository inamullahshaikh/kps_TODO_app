from src.app import App
def main():
    app = App()

    while True:
        print("\n===== MAIN MENU =====")
        print("1. Sign Up")
        print("2. Log In")
        print("3. View Logged-in User")
        print("4. Update User")
        print("5. Create Namespace")
        print("6. Add User to Namespace")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            email = input("Enter Email: ")
            phone = input("Enter Phone Number: ")
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            app.Signup_user(name, age, email, phone, username, password)
            print("User signed up successfully!")

        elif choice == '2':
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            app.Login(username, password)
            if app._logged_in_user:
                print("Login successful!")
            else:
                print("Invalid username or password.")

        elif choice == '3':
            app.view_user()

        elif choice == '4':
            app.update_user()

        elif choice == '5':
            if app._logged_in_user:
                app.create_namespace()
            else:
                print("You must be logged in to create a namespace.")

        elif choice == '6':
            if app._logged_in_user:
                app.add_user_to_namespace()
            else:
                print("You must be logged in to add users to a namespace.")

        elif choice == '0':
            print("Exiting the application...")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == '__main__':
    main()