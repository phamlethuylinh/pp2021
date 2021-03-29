def input_number_student():
    nb_s = int(input("Enter the numbers of student:"))
    return nb_s


def input_info_student(nb_s):
    na_s = []
    id_s = []
    dob_s = []
    for n in range(nb_s + 1):
        name = int(input("\nName:"))
        na_s += name
        i = int(input("\nId"))
        id_s += i
        dob = int(input("\nDate of bird"))
        dob_s += dob
    return [na_s, id_s, dob_s]


def output_list_student(a, m):
    print("\nThe list of info is: ")
    for n in range(a):
        print(m[0][n] + "|" + m[1][n] + "|" + m[2][1])


def input_number_courses():
    n = int(input("Enter the number of Course:"))
    return n


def input_info_courses(a):
    id_c = []
    na_c = []
    for n in range(0, a, 1):
        print("Enter info of course: ", n+1)
        idc = input("Id")
        id_c += idc
        nam = input("Name of course:")
        na_c += nam
    return [id_c, na_c]

    def list_of_courses(b,k):
    print("\tThe list of courses' info is:")
    for n in range(b):
        print(k[0][n]+"|"+k[1][n])


def input_mark(a, b, m, k,):
    mark_s = []
    print("\ncourse Id:")
    list_of_courses(b,k)
    cx = int(input())
    id_c = k[0][cx - 1]

    print("Enter student's marks:")
    for n in range(a):
        id_s = m[0][n]
        mark = int(input("mark of student: \t" + id_s + m[1][n] + "\t"))
        mark_s += [id_c, id_s, mark]
    print("\nThe marks of students " + k[1][cx - 1] + " are:")
    return mark_s


e = input_number_student()
f = input_info_student(e)
output_list_student(e, f)

g = input_number_courses()
h = input_info_courses(g)
list_of_courses(g, h)

u = input_mark(e, g, f, h)
print(u)
