
import math

import curses

import numpy as np


class Student:
    def __init__(self, id_s, name_s, dob):
        self.id_s = id_s
        self.name = name_s
        self.dob = dob
        Student.append(self)
        Student_ID.append(self.id)
        self.marks = {}

    def add_id(self):
        return self.id_s

    def add_name(self):
        return self.name_s

    def add_dob(self):
        return self.dob

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

class show:
    def num_Of_Student(self):
        while True:
            py.renum()
            Num = int(py.getstr().decode())
            if Num <= 0:
                curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
                py.addstr("Does not exits!!!\n", curses.color_pair(1))
                py.refresh()
                curses.napms(1000)
                py.clear()
                py.refresh()
            else:
                return Num

    def num_Of_Course(self):
        while True:
            py.renum()
            Numco = int(py.getstr().decode())
            if Numco <= 0:
                curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
                py.addstr("Does not exits!!!\n", curses.color_pair(1))
                py.refresh()
                curses.napms(1000)
                py.clear()
                py.refresh()
            else:
                return Numco

    def InfoOfstudent(self):
        py.addstr("Enter ID of Student:")
        py.refresh()
        id_s = py.getstr().decode()

        py.addstr("Enter Name of Student:")
        py.refresh()
        name = py.getstr().decode()

        py.addstr("Enter date of brith:")
        py.refresh()
        dob = py.getstr().decode()
        Student(id_s, name_s, dob)

    def InfoOfcourse(self):
        py.addstr("Enter ID of Course:")
        py.refresh()
        id_c = py.getstr().decode()
        py.addstr("Enter Name of Course:")
        py.refresh()
        name_c = py.getstr().decode()
        py.addstr("Enter Number Credits Course:")
        py.refresh()
        credits = float(py.getstr().decode())
        Course(id_c, name_c, credits)


py.addstr("Enter ID of Course:")
py.refresh()
id_c = py.getstr().decode()

py.addstr("Enter Name of Course:")
py.refresh()
name_c = py.getstr().decode()

py.addstr("Enter CourseCredit:")
py.refresh()
credits = float(py.getstr().decode())
Course(id_c, name_c, credits)