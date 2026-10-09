'''
It demonstrates weak aggregation between a department and a teacher.

In this example, the `Dept` class stores a reference to a `Teacher` object,
but it does not create or own that teacher. The teacher is created outside
of the department and then passed in. This is a loose association, which is
known as weak aggregation.

'''

class Teacher:
    '''It represents a teacher that can exist independently.

    The teacher object is not controlled by any department. It can be used in
    different places without being tightly coupled to one container.
    '''
    def __init__(self, name):
        self.name = name
    def teach(self):
        print(self.name, "is teaching.")

class Dept:
    '''It represents a department that aggregates a teacher reference.

    This is weak aggregation because the department simply keeps a reference to
    a `Teacher` object and does not own its lifecycle. The teacher may still
    exist even if the department is removed or changed.
    '''
    def __init__(self, teacher):
        self.teacher = teacher

teacher1 = Teacher("Mr. Smith")
dept = Dept(teacher1)
dept.teacher.teach()