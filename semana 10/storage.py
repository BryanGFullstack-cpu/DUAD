#storage


import csv
from os.path import exists
from data import students


FILE_NAME = 'students_data.csv'
sections = ['Name', 'section', 'spanish', 'english', 'social', 'science']

def export_to_csv():
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(sections)
        for student in students:
            writer.writerow([
                students['name'],
                students['section'],
                students['spanish'],
                students['english'],
                students['social science']
            ])

print(f"Data exported successfully to {FILE_NAME}")

def import_from_csv():
    if not exists(FILE_NAME):
        print("No data file found to import.")
        return

    with open(FILE_NAME, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({
                'name': row['Name'],
                'section': row['section'],
                'spanish': float(row['spanish']),
                'english': float(row['english']),
                'social': float(row['social']),
                'science': float(row['science'])
            })

    print("Data imported successfully from", FILE_NAME)