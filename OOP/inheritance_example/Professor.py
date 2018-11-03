from BabsonPerson import BabsonPerson
from Person import Person

class Professor(BabsonPerson):

    def __init__(self, name, department):
        BabsonPerson.__init__(self, name)
        self.department = department
    
    def get_department(self):
        return self.department
    
    def lecture(self, lesson):
        return BabsonPerson.speak(self, "Listen up class. Always make sure to keep the following statement in mind: " + lesson)