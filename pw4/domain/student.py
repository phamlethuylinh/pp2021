
class Student:
    def __init__(self, id_s, name_s, dob):
        self.id_s = id_s
        self.name = name_s
        self.dob = dob
        Student.append(self)
        Student_ID.append(self.id_s)
        self.marks = {}

    def add_id(self):
        return self.id_s

    def add_name(self):
        return self.name_s

    def add_dob(self):
        return self.dob
