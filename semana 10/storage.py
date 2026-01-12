#storage


import csv
from os.path import exists


FILE_NAME = "students_data.csv"
HEADERS = ["name", "section", "spanish", "english", "socials", "science"]

def save_students_csv(students):
    with open(FILE_NAME, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(HEADERS)

        for student in students:
            writer.writerow([
                student["name"],
                student["section"],
                student["spanish"],
                student["english"],
                student["socials"],
                student["science"]
            ])

    print(f"Data exported successfully to {FILE_NAME}")

def import_from_csv(students):
    if not exists(FILE_NAME):
        print("No data file found to import.")
        return

    with open(FILE_NAME, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({
                "name": row["name"],
                "section": row["section"],
                "spanish": int(row["spanish"]),
                "english": int(row["english"]),
                "socials": int(row["socials"]),
                "science": int(row["science"])
            })

    print(f"Data imported successfully from {FILE_NAME}")
