#utils

import re

def is_valid_name(name):
    return name.replace(" ", "").isalpha()

def is_valid_section(section):
    return bool(re.match(r"^[0-9]{2}[A-Z]$", section))

def get_valid_name():
    while True:
        name = input("Enter name: ").strip()
        if is_valid_name(name):
            return name
        print("Invalid name. Must contain only letters.")

def get_valid_section():
    while True:
        section = input("Enter section (e.g., 11B): ").strip().upper()
        if is_valid_section(section):
            return section
        print("Invalid section format. Must be two digits followed by a letter.")
