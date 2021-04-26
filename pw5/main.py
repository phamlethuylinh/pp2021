import curses
from output import outputs
from input import inputs
from domain.Student import *
from domain.Course import *
from domain.Mark import *

py = curses.initscr()
curses.start_color()

file_name = "student.dat"
with zipfile.ZipFile(file_name, "r") as zip:
    zip.extractall()
    
f = open("/home/phamlethuylinh/pp2021/pw5/students.txt")


s = int(numberofstudent())
m = 1
while m <= s:
    m += 1
    student_info()
student()
c = int(course_num())
p = 1
while p <= c:
    p += 1
    add_course()
course()
mark()
f = open("/home/phamlethuylinh/pp2021/pw5/students.txt")


print("  Choose  ")
print("1=YESsss")
print("2=NOooo")
for i in range(0, len(course)):
    ca = int(input(" Enter your choose: "))
    if ca == 1:
        print(" Mark of the student ")
        mark()
        break
    else:
        zip_file = zipfile.ZipFile("student.dat", "w", zipfile.ZIP_DEFLATED)
        zip_file.write("student.txt")
        zip_file.write("course.txt")
        zip_file.write("mark.txt")
        break
l = ave_gpa()
l.getave_gpa()
calculate_mark()
