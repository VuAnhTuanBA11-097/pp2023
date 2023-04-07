import math
# Input functions
class student:
    def __init__(self,stu_id, stu_name, stu_dob):
        self.stu_id = stu_id
        self.stu_name =stu_name
        self.stu_dob = stu_dob
    def accept(self):
        stu_id=input('enter the ID of student :')
        stu_name=input('enter the name of student :')
        stu_dob=input('enter ther dob of student :')
        stu=student(stu_id,stu_name,stu_dob)
        students.append(stu)
        return students
    def display(self, stu):
        print("Name : ", stu.stu_name)
        print("ID : ", stu.stu_id)
        print("DOB : ", stu.stu_dob)
    def get_id(self,stu):
        return stu.stu_id
class course:
    def __init__(self,cour_id,cour_name): 
        self.cour_id=cour_id
        self.cour_name=cour_name
    def accept(self):
        cour_id=input('enter the id of course :')
        cour_name=input('enter the name of course :')
        cour=course(cour_id,cour_name)
        courses.append(cour)
    def display(self,cour):
        print("Name of course:",cour.cour_name)
        print("ID of course :",cour.cour_id)
    def get_id(self,cour):
        return cour.cour_id
        

    
# show list      
students=[]
stud = student(0,0,0)
num_stu=int(input('enter the number of student:'))
for x in range (num_stu):
    stud.accept()
print("\n")
print("\nList of Students\n")
for i in range(students.__len__()):
    stud.display(students[i])
courses=[]
cou=course(0,0)
num_cour=int(input('enter the number of course :'))
for x in range (num_cour):
    cou.accept()
print("\n")
print('\nlist of course :\n')
for x in range (courses.__len__()):
    cou.display(courses[i])
marks={}
marks_cour = {}

GPA_student={}
for x in range(students.__len__()):
    stu_id=input('enter the id of student to add the scores:')
    GPA=0
    GPA1=0
    for x in range (courses.__len__()):
        cour_id=cou.get_id(courses[x])
        mar = float(input(f'enter the mark for course {cour_id}:'))
        mark =math.floor(mar)
        marks_cour[cour_id]=mark
        GPA=GPA+mark
        GPA1=GPA/num_cour
        GPA_student[stu_id]=GPA1
        marks[stu_id] =marks_cour.copy()
    GPA_sorted=sorted(GPA_student.items())
print("\n")
print("\n list of mark :\n")
print(marks)
print('\nthe GPA for student :\n')
print(GPA_sorted)
