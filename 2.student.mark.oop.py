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
def mymark(GPA,GP1):
    return GPA, GP1
while True:
    print("1. Enter information of student:")
    print("2. Enter information od course:")
    print("3. Enter the mark :")
    print("4. List student:") 
    print("5. List course:")
    print("6. List mark")
    print("0. Exit: ")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        students=[]
        stud = student(0,0,0)
        num_stu=int(input('enter the number of student:'))
        for x in range (num_stu):
            stud.accept()
    elif choice == 2:
        courses=[]
        cou=course(0,0)
        num_cour=int(input('enter the number of course :'))
        for x in range (num_cour):
            cou.accept()
    elif choice == 3:
        marks={}
        marks_stu = {}
        for x in range(num_cour):
            cour_id=input('enter the id of course:')
            for x in range (students.__len__()):
                stu_id=stud.get_id(students[x])
                mark = float(input(f'enter the mark for student {stu_id}:'))
                marks_stu[stu_id]=mark
                marks[cour_id] =marks_stu.copy()
    elif choice ==4:
        print("\n")
        print("\nList of Students\n")
        for i in range(students.__len__()):
            stud.display(students[i])
    elif choice ==5:
        print("\n")
        print('\nlist of course :\n')
        for x in range (courses.__len__()):
            cou.display(courses[i])
    elif choice ==6:
        print("\n")
        print("\n list of mark :\n")
        print(marks)
    elif choice == 0:
        break





