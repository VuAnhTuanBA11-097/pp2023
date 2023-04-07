def input_student():
    students = []
    num_student = int(input('enter the numbers of student:'))
    for x in range(num_student):
        id_student = input('enter the id of student:')
        name_student = input('enter the name of student:')
        dob_student = input('enter the date of birth student:')
        students.append((id_student,name_student,dob_student))
    return students
A = input_student()    
def input_course():
    course = []
    num_course=int(input('enter the numbers of course:'))
    for x in range(num_course):
        id_course = input ('enter the id of course:')
        name_course = input ('enter the name of course:')
        course.append(id_course)
        course.append(name_course)
    return course
B = input_course()
def input_mark(A):
    mark = {}
    mark_stu = {}
    num_course=int(input('enter the numbers of course:'))
    for x in range(num_course):
        course_id = input("Enter the course ID: ")
        for x in A:
            student_id = x[0]
            marks = float(input(f"Enter the mark for student {student_id}: "))
            mark_stu[student_id] = marks
            mark[course_id]=mark_stu.copy()
    return mark
C=input_mark(A)
def list_student(A):
    print('this is your list student:')
    print(A)
list_student(A)
def list_course(B):
    print('this is the list of course:')
    print(B)
list_course(B)
def show_mark(C,B):
    course_id = input("please Enter the course ID youk wAnt to see: ")
    print('the mark of course is:')
    print(C[course_id])
show_mark(C,B)