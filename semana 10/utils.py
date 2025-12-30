#utils

def is_valid_name(name):
    return 2<= len(name) <=30 and name.replace(" ", "").isalpha()

def is_valid_section(section):
    return len(section) ==1 and section.isalpha()

def get_valid_name():
    while True:
        name= input("Enter name: ").strip()
        if is_valid_name(name):
            return name
        print("Invalid name. Must be 2-30 letters.")

        def get_valid_section():
            while True:
                section= input("Enter section (A-Z): ").strip().upper()
                if is_valid_section(section):
                    return section
                print("Invalid section. Must be a single letter.")