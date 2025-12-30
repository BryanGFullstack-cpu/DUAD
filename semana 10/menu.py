#menu


from actions import (
    add_student,
    show_all_students,
    show_top_three,
    show_global_average,
    delete_student,
    show_failed_students,
)

def show_menu():
    while True:
        print("\n—— Student Management Menu ——")
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Show Top Three Students")
        print("4. Show Global Average")
        print("5. Delete Student")
        print("6. Show Failed Students")
        print("7. Exit")

        choice = input("Select an option (1-7): ").strip()
        if not choice.isdigit() or not (1 <= int(choice) <= 7):
            print("Invalid option. Please enter a number between 1 and 7.")
            continue

        if choice == '1':
            add_student()
        elif choice == '2':
            show_all_students()
        elif choice == '3':
            show_top_three()
        elif choice == '4':
            show_global_average()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            show_failed_students()
        elif choice == '7':
            print("Exiting the program.")
            break