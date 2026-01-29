#mainn


from cvs_Manager import load_students_from_csv, save_students_to_csv
from menu import handle_menu

FILENAME = "students.csv"

def main():
    students = load_students_from_csv(FILENAME)

    def save():
        save_students_to_csv(FILENAME, students)

    handle_menu(students, save)

main()
