class Course:
    def __init__(self,courseName,courseLanguage,courseDuration):
        self.courseName = courseName
        self.courseLanguage = courseLanguage
        self.courseDuration = courseDuration

    def details(self):
        print("Course Name=",self.courseName)
        print("Course Language=",self.courseLanguage)
        print("Course Duration=",self.courseDuration)


class Student:
    def __init__(self,studentName,studentId,studentDob):
        self.studentName = studentName
        self.studentId = studentId
        self.studentDob = studentDob

    def details(self):
        print("Student Name=",self.studentName)
        print("Student ID=",self.studentId)
        print("Student DOB=",self.studentDob)


def poly_morphism(ob):
    ob.details()

cour = Course("FSDS","Python",1)
stud = Student("Atanu",1,"26/07/1991")
poly_morphism(cour)
poly_morphism(stud)