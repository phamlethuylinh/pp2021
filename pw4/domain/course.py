class Course:
    def __init__(self, id_c, name_c, credits):
        self.id_c = id_c
        self.name_c = name_c
        self.credits = credits
        Courses.append(self)
        Courses_ID.append(self.id_c)
        Courses_credits.append(self.credits)

    def add_id(self):
        return self.id_c

    def add_name(self):
        return self.name_c

    def add_credits(self):
        return self.credits