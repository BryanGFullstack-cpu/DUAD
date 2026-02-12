#Actionss


from models import Student

def action_add_student(students):
    name = input("Name: ")
    section = input("Section: ")
    spanish = int(input("Spanish Grade: "))
    english = int(input("English Grade: "))
    socials = int(input("Socials Grade: "))
    science = int(input("Science Grade: "))
    student = Student(name, section, spanish, english, socials, science)
    students.append(student)
    print("Student added successfully.")


def action_show_all(students):
    if not students:
        print("No students registered.")
        return

    for s in students:
        print(f"{s.name} - {s.section} - Average: {s.get_average():.2f}")

def action_search_student(students):
    name = input("Enter the name to search: ")

    for s in students:
        if s.name.lower() == name.lower():
            print(f"Found: {s.name} - {s.section}")
            print(f"Grades: Spanish {s.spanish}, English {s.english}, Socials {s.socials}, Science {s.science}")
            return

    print("Student not found.")