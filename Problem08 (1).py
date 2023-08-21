#QUESTION01
#DESIGN CLASS
class Student:
    def __init__(self, name='Just a student', dept='nothing'):
        self.__name = name
        self.__department = dept
    def set_department(self, dept):
        self.__department = dept
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
    def __str__(self):
        return 'Name: '+self.__name+' Department: '+self.__department

#DESIGN CLASS
class BBA_Student():
    def __init__(self, department = "default"):
        self.dept = Student (department,"BBA")
    def __str__(self):
        return str(self.dept)

#MAINCODE
print(BBA_Student())
print(BBA_Student('Humpty Dumpty'))
print(BBA_Student('Little Bo Peep'))