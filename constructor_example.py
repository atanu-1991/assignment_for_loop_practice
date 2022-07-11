class Company:
    def __init__(self,name,course,type,year):
        self.name = name
        self.course = course
        self.type = type
        self.year = year


ob = Company("Ineuron","FSDS","IT","2022")
print(ob.name)
print(ob.course)
print(ob.type)
print(ob.year)