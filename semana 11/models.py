#models


class Student:
    def __init__(self, name, section, spanish, english, socials, science):
        self.name = name
        self.section = section
        self.spanish = spanish
        self.english = english
        self.socials = socials
        self.science = science

    def get_average(self):
        return (self.spanish + self.english + self.socials + self.science) / 4

    def to_dict(self):
        return {
            "name": self.name,
            "section": self.section,
            "spanish": self.spanish,
            "english": self.english,
            "socials": self.socials,
            "science": self.science
        }
