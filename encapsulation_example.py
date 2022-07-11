class Course:
    def __init__(self,id,name,course_name,year):
        self.id = id
        self.__name = name
        self.course_name = course_name
        self.year = year


    def name_change(self,new_name):
        self.__name = new_name


    def new_name(self):
        print("New Name is", self.__name)


obj = Course(1,"Atanu Kundu","FSDS",2022)
obj.new_name()
obj.name_change("Shaeb Kundu")
obj.new_name()