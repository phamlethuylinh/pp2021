class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}

    def add_id(self):
        return self.id

    def add_name(self):
        return self.name

    def add_dob(self):
        return self.dob

    def add_mark(self):
        return self.marks

    def set_id(self, _id):
        self.id = _id

    def set_name(self, name):
        self.name = name

    def set_dob(self, dob):
        self.dob = dob

    def set_mark(self, course, mark):
        self.marks.update({course: mark})

    def displayStudent(self):
        print("Student ID: " + self.id)
        print("Student name: " + self.name)
        print("Student DoB: " + self.dob)


    def displayMark(self, course):
        print("Mark of " + self.name + ":" + str(self.marks.get(course)))





class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def add_id(self):
        return self.id

    def add_name(self):
        return self.name

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def display_Course(self):
        print("Course ID: " + self.id)
        print("Course name: " + self.name)

def num_Of_Student():
    while True:
        try:
            std_num = int(input("Enter number of students : "))
            return std_num
        except ValueError:
            print("Invalid number.")


def InfoOfstudent():
    std_id = input("Student ID: ")
    std_name = input("Name: ")
    std_dob = input("Date of birth: ")
    return std_id, std_name, std_dob
def num_Of_Course():
    while True:
        try:
            course_num = int(input("Number of courses: "))
            return course_num
        except ValueError:
            print("ERR number.")
def InfoOfcourse():
    course_id = input("Course ID: ")
    course_name = input("Course name: ")
    return course_id, course_name


def find_Course_Name(courses, course_id):
    for course in courses:
        if course.get_id() == course_id:
            return course.get_name()
    print("Can't find ID.\n ReenterID. Thanks!")


if __name__ == "__main__":
    students = []
    courses = []

    student_num = num_Of_Student()
    print(student_num)
    for i in range(0, student_num):
        id, name, dob = InfoOfstudent()
        students.append(Student(id, name, dob))

    course_num = num_Of_Course()
    for i in range(0, course_num):
        id, name = InfoOfcourse()
        courses.append(Course(id, name))

    print("Display information of students:\n\n\n")
    for student in students:
        student.display_Student()

    print("Display information of courses:\n\n\n")
    for course in courses:
        course.display_Course()

    x = 'Y'
    while x == 'Y':
        sel_course_id = input("A course ID: ")
        sel_course = find_Course_Name(courses, sel_course_id)
        print("Course name: " + sel_course + "\n")
        for student in students:
            mark = input("Enter " + student.name + "'s mark: ")
            student.set_mark(sel_course, mark)
        x = input("Another course:Enter:'Y' \n")
    sel_course_id = input("Select a displayed course ID: ")
    sel_course = find_Course_Name(courses, sel_course_id)
    print(f"Display students' marks of course {sel_course}:\n")
    for student in students:
        student.display_Mark(sel_course)