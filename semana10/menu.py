#menu

from actions import (
    add_students,
    show_all_students,
    show_top_three,
    show_global_average,
    delete_student,
    show_failed_students,
)
from storage import save_students_csv, import_from_csv

def show_menu(students):
    while True:
        print("\n—— Student Management Menu ——")
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Show Top Three Students")
        print("4. Show Global Average")
        print("5. Delete Student")
        print("6. Show Failed Students")
        print("7. Export Students to CSV")
        print("8. Import Students from CSV")
        print("9. Exit")

        choice = input("Select an option (1-9): ").strip()

        if not choice.isdigit() or not (1 <= int(choice) <= 9):
            print("Invalid option. Please enter a number between 1 and 9.")
            continue

        if choice == '1':
            add_students(students)
        elif choice == '2':
            show_all_students(students)
        elif choice == '3':
            show_top_three(students)
        elif choice == '4':
            show_global_average(students)
        elif choice == '5':
            delete_student(students)
        elif choice == '6':
            show_failed_students(students)
        elif choice == '7':
            save_students_csv(students)
        elif choice == '8':
            import_from_csv(students)
        elif choice == '9':
            print("Exiting the program.")
            break