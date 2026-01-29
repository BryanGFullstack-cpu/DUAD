import csv
from models import Student

def load_students_from_csv(filename):
    students = []
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = Student(
                    row["name"],
                    row["section"],
                    int(row["Spanish"]),
                    int(row["English"]),
                    int(row["Socials"]),
                    int(row["Science"])
                )
                students.append(student)
    except FileNotFoundError:
        pass

    return students


def save_students_to_csv(filename, students):
    with open(filename, "w", newline="") as file:
        fieldnames = ["name", "section", "Spanish", "English", "Socials", "Science"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for student in students:
            writer.writerow(student.to_dict())
