students=[]
def AddStudent(name):
    students.append(name)
    print(f"{name} has been added to the class.")

def RemoveStudent(name):
    if name in students:
        students.remove(name)
        print(f"{name} has been removed from the class.")
    else:
        print(f"{name} is not in the class.")

def DisplayStudents():
    if students:
        print("The students in the class are:")
        for student in students:
            print(student)

AddStudent("Ali")
AddStudent("Ahmed")
AddStudent("Waleed")
DisplayStudents()
RemoveStudent("Waleed")
DisplayStudents()