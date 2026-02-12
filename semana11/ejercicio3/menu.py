#Menuu


from actions import (
    action_add_student,
    action_show_all,
    action_search_student
)

def show_menu():
    print("\n--- STUDENT MANAGEMENT SYSTEM ---")
    print("1. Add student")
    print("2. Show all students")
    print("3. Search student")
    print("4. Save and exit")

def handle_menu(students, save_function):
    while True:
        show_menu()
        option = input("Select an option: ")

        if option == "1":
            action_add_student(students)

        elif option == "2":
            action_show_all(students)

        elif option == "3":
            action_search_student(students)

        elif option == "4":
            save_function()
            print("Data saved. Exiting...")
            break

        else:
            print("Invalid option.")