#student management system
#---------------------------

#login requirement
#------------------

#username:admin
#password:1234
#if correct -> show menu
#else -> show errror


#use dictionary like:
# students={
#     "101":{"name":"arun","age":20,"course":"python"}
# }

#Add student
#-----------
#enter student id
#if already exists show error
#else add:



# ==================================================
# code
# ==================================================
cUsername="admin"
cPassword="1234"

students={}

def login():
    userName=input("Enter the username\n")
    password=input("Enter the password\n")
    if userName==cUsername and password==cPassword :
        return True
    else:
        return False
    
def homePage():
    while True:
        print("Enter the operations to be performed")
        print("1.Add Student")
        print("2.Delete Student")
        print("3.Edit Student")
        print("4.view Student")
        print("5.search Student")
        print("6.exit")
        getInput=input()
        if getInput=="1":
            addStudent()
        elif getInput=="2":
             delStudent()
        elif getInput=="3":
            editStudent()
        elif getInput=="4":
            showStudent()
        elif getInput=="5":
            searchStudent() 
        elif getInput=="6":
            print("Exiting...")
            return
        else:
            print("Enter a vaild input")           



def addStudent():
    print("Enter the student details :")
    id=input("Enter the student id\n")
    name=input("Enter the student name\n")
    age=input("Enter the student age\n")
    course=input("Enter the student course\n")
    students.update({id:{"name":name,"age":age,"course":course}})
    print("student added successfully")

def delStudent():
    deleteStudent=input("Enter the student id to be deleted")
    del students[deleteStudent]
    print("student deleted successfully")    

def editStudent():
    editUser=input("Enter the student id to be edited")
    if editUser not in students.keys():
        print("student is not present")
        return
    name=input("Enter the student name\n")
    age=input("Enter the student age\n")
    course=input("Enter the student course\n")
    students.update({editUser:{"name":name,"age":age,"course":course}})
    print("student updated...")

def showStudent():
    print("==============================")
    print("List of all students")
    print("==============================")
    print(students)

def searchStudent():
    id=input("Enter the student id to be searched")
    
    if id not in students.keys():
        print("there is no student with such id")
        return
    fetchedStudent=students[id]
    print("==============================")
    print("student detail of id",id)
    print("==============================")   
    print("name",fetchedStudent["name"])
    print("age",fetchedStudent["age"])
    print("course",fetchedStudent["course"])

# if login():
#     homePage()

aset = {1, 2, 4}
aset.update(["5"])
print(aset)