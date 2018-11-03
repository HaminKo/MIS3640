class Student:
    """
    Represents a student

    attributes: first_name, last_name, credits, GPA, major, current_classes
    """

    def __init__(self, first_name = 'John', last_name = 'Doe', credits = 0, GPA = 0, major = 'none', current_classes = [], all_classes = {}):
        self.first_name = first_name
        self.last_name = last_name
        self.credits = credits
        self.GPA = GPA
        self.major = major
        self.current_classes = current_classes
        self.all_classes = all_classes
            
    def __string__(self):
        return '{} {}, major:{}'.format(self.first_name, self.last_name, self.major)
    
    def __add__(self, other):
        self.GPA += other.GPA
    
    def add_class_description(self, class_description):
        """
        class_description is an object with the following attributes:

        name, professor, course_code, grade, credits
        """
        return self.current_classes.append(class_description)
    
    def add_class(self):
        for course in self.current_classes:
            self.all_classes[course.name] = course
    
    def remove_current_class(self, course):
        self.current_classes.remove(course)