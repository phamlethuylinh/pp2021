import math
import curses
import numpy as np
from domain.Student import *
from domain.Course import *
from domain.Mark import *

py = curses.initscr()
curses.start_color()

class inputs():
    def numberofstudent(self):
        student_num = int(input("Enter the number of student:"))
        if (student_num <= 0):
            print("Error")
            return 'False'
        else:
            return student_num

    def student_info(self):
        print(" Student Info ")

        id_s = input("Enter the ID:")
        name_s = input("Enter the student name:")
        dob = input("Enter the dob student:")
        info_s = {
            'id': id_s,
            'name': name_s,
            'dob': dob
        }
        Student_ID.append(id_s)
        Student.append(info_s)
    def number_course(self):
        print(" Number of Course: ")
        course_num = int(input("Enter the number of course :"))
        if (course_num <= 0):
            print("Doesn't exits \n Find error")
            return 0
        else:
            return course_num

    def add_courses(self):
        name_c = input("Enter the name of course:")
        id_c = input("Enter the ID of course: ")
        credits = input("Enter the number credits are:")
        course_set = {
            'credits': credits,
            'name': name_c,
            'id': id_c
        }
        Course.append(course_set)
        Course_ID.append(id_c)

    def mark(self):
        x = 1
        val = len(Student)
        while x <= val:
            x += 1
            n = input("Enter the ID of Student: ")
            if a in Student_ID:
                for i in range(0, len(Course)):
                    b = input("Enter the ID of Course: ")
                    if b in Course_ID:
                        mark = math.floor(float(input("Enter mark of Student: ")))
                        note = {
                            'a': a,
                            'b': b,
                            'mark': mark

                        }
                    else:
                        print("ID of Student is incorrect!!!")
                        break
                    Mark.append(note)

            else:
                print("ID course is incorrect!!! ")
                break

    def ave_gpa(self):
        print(" Ave of Gpa ")
        value = np.array([self.mark])
        cd = np.array([self.credit])
        ag = input("Enter the ID student:")
        if ag in self.id:
            for i in range(len(Mark)):
                gpa = value[i] / cd[i]
                return gpa
        print(gpa)

    def calculate_mark(self):
        print("===== FIND GPA OF STUDENT ======")
        cal = input("Enter the ID:")
        if cal in self.id:
            marks = input("Enter the mark:")
        Mark.append(marks)

        cre_value = [Credit]
        mark_val = [Mark]
        name = input(" Enter the name of student: ")
        gpa = mark_val / cre_value
        return gpa