from School import Student

def getStudentInfoFromUser(currentNumber):
    print("Enter information for student {}".format(currentNumber))
    name = input("Name: ")
    age = input("Age: ")
    gender = input("Gender: ")
    cls = input("Class: ")
    return Student(name, age, gender, cls)


num = int(input("Please add the number of students you want to add data for : "))

students = []
for i in range(0,num):
    students.append(getStudentInfoFromUser(i+1))

with open("students.csv","a") as file:
    file.write("\n".join(str(student) for student in students))