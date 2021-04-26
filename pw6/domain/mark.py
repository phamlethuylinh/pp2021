class Marks:
    def __init__(self, id_c, id_s, marks, gpa=0):
        self.id_c = id_c
        self.id_s = id_s
        self.marks = marks
        self.gpa = gpa
        Mark.append(self)
        Mark_s.append(self.marks)

    def add_cid(self):
        return self.id_c

    def add_sid(self):
        return self.id_s

    def add_marks(self):
        return self.marks

    def add_gpa(self):
        return self.gpa

    def set_gpa(self, gpa):
        self.gpa = gpa