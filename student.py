from module import *
from moduleElement import *


class Student(object):
    def __init__(self, name):
        self.name = name
        self.modules = []
        self.grades = {}

    def add_module(self, module):
        self.modules.append(module)
        self.grades[module.get_title()] = module.get_grade()

    def get_list_modules(self):
        print("\nModules for student %s:" % self.name)
        for module in self.modules:
            print(module)

    def get_grades(self):
        print("\nGrades for student %s:" % self.name)
        for grade in self.grades:
            print("%s: %d" %(grade, self.grades[grade]))


### test cases ###

fabio = Student("Fabio Meier")
fabio.add_module(info1)
fabio.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#	Info 1

fabio.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#	Info 1: 6
