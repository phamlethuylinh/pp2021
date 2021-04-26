
import curses

from domain.Student import*
from domain.Course import*
from domain.Mark import*


class output():
    def student_info(self):
        print(" List of student ")
        for i in range(0, len(Student)):
            print(f"ID:{Student[i]['id']} name:{Student[i]['name']} DoB:{Student[i]['dob']}")

    def s_course(self):
        print(" List of course ")
        for i in range(0, len(Course)):
            print(f"ID:{Course[i]['id']}  Name :{Course[i]['name']} Credits:{Course[i]['cd']}")

    def s_mark(self):
        print(" List mark ")
        for i in range(0, len(Mark)):
            print(f"ID-course: {Mark[i]['b']} ID-Student: {Mark[i]['a']}  mark:{Mark[i]['mark']}")

    def GPA(self):
        arr = np.array([gpa_s])
        arr[::-1].sort()
        print("The list is %s:\n" % (arr))