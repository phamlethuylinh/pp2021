import curses
from output import outputs
from input import inputs
from domain.Student import *
from domain.Course import *
from domain.Mark import *

py = curses.initscr()
curses.start_color()

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
        break
l = ave_gpa()
l.getave_gpa()
calculate_mark()