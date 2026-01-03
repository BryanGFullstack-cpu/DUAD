#actiones

import re
from data import students


def is_valid_name(name):
    return name.replace(" ", "").isalpha()

def is_valid_section(section):
    return bool(re.match(r"^[0-9]{2}[A-Z]$", section))

def student_exists(name, section):
    for s in students:
        if s["name"].lower() == name.lower() and s["section"] == section:
            return True
    return False

def get_valid_grade(subject):
    while True:
        try:
            grade = int(input(f"Enter grade for {subject}: "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid number. Try again.")



def add_students():
    n = int(input("How many students do you want to add? "))

    for _ in range(n):
        print("\n--- New Student ---")

        # Name
        while True:
            name = input("Full name: ").strip()
            if is_valid_name(name):
                break
            print("Invalid name. Must contain only letters.")

        # Section
        while True:
            section = input("Section (e.g., 11B): ").strip().upper()
            if is_valid_section(section):
                break
            print("Invalid section format.")

        # Check duplicates
        if student_exists(name, section):
            print("This student already exists. Skipping.")
            continue

        # Grades
        spanish = get_valid_grade("Spanish")
        english = get_valid_grade("English")
        socials = get_valid_grade("Socials")
        science = get_valid_grade("Science")

        new_students = {
            "name": name,
            "section": section,
            "spanish": spanish,
            "english": english,
            "socials": socials,
            "science": science
        }

        students.append(new_students)
        print("Student added successfully!")

def show_all_students():
    if not students:
        print("No students registered.")
        return

    for s in students:
        print(f"{s['name']} - {s['section']} | "
              f"ES:{s['spanish']} EN:{s['english']} SO:{s['socials']} SC:{s['science']}")

def show_top_three():
    if len(students) < 3:
        print("Not enough students to show top 3.")
        return

    sorted_students = sorted(
        students,
        key=lambda s: (s["spanish"] + s["english"] + s["socials"] + s["science"]) / 4,
        reverse=True
    )

    print("\n--- TOP 3 STUDENTS ---")
    for i, s in enumerate(sorted_students[:3], start=1):
        avg = (s["spanish"] + s["english"] + s["socials"] + s["science"]) / 4
        print(f"{i}. {s['name']} ({s['section']}) - Average: {avg:.2f}")

def show_global_average():
    if not students:
        print("No students registered.")
        return

    total = 0
    for s in students:
        avg = (s["spanish"] + s["english"] + s["socials"] + s["science"]) / 4
        total += avg

    global_avg = total / len(students)
    print(f"Global average: {global_avg:.2f}")

def delete_student():
    name = input("Enter student name: ").strip()
    section = input("Enter section: ").strip().upper()

    for s in students:
        if s["name"].lower() == name.lower() and s["section"] == section:
            confirm = input("Are you sure you want to delete this student? (y/n): ")
            if confirm.lower() == "y":
                students.remove(s)
                print("Student deleted.")
            else:
                print("Cancelled.")
            return

    print("Student not found.")

def show_failed_students():
    failed = []

    for s in students:
        failed_subjects = {
            subj: s[subj] for subj in ["spanish", "english", "socials", "science"]
            if s[subj] < 60
        }
        if failed_subjects:
            failed.append((s, failed_subjects))

    if not failed:
        print("No failed students.")
        return

    print("\n--- FAILED STUDENTS ---")
    for s, subjects in failed:
        print(f"{s['name']} ({s['section']}) - Failed:")
        for subj, grade in subjects.items():
            print(f"  {subj}: {grade}")