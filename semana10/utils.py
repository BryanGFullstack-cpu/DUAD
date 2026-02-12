#utils

import re

def is_valid_name(name):
    # Acepta nombres con espacios, pero solo letras
    cleaned = name.replace(" ", "")
    return cleaned.isalpha() and len(cleaned) >= 2

def is_valid_section(section):
    # Formato: dos números + una letra mayúscula (ej: 11B)
    return bool(re.match(r"^[0-9]{2}[A-Z]$", section))

def get_valid_name():
    while True:
        name = input("Enter full name: ").strip()
        if is_valid_name(name):
            return name
        print("Invalid name. Use only letters and spaces.")

def get_valid_section():
    while True:
        section = input("Enter section (e.g., 11B): ").strip().upper()
        if is_valid_section(section):
            return section
        print("Invalid section. Format must be two digits + one letter (e.g., 10A).")