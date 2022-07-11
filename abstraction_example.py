class Course:
    def __init__(self,id,course_name,year):
        self.__id = id
        self.course_name = course_name
        self.year = year

class Student(Course):
    def __init__(self,name,*args):
        super(Student,self).__init__(*args)
        self.name = name

    def student_details(self):
        print("Name of the Student is",self.name)
        print("Name of the Course is",self.course_name)
        print("Year of Admmission",self.year)

ob = Student("Atanu Kundu",1,"FSDS",2022)
ob.student_details()