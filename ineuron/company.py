class Course:
    def __init__(self,courseName,courseYear,courseDuration):
        self.courseName = courseName
        self._courseYear = courseYear
        self.__courseDuration = courseDuration


ob = Course("FSDS","2022","1 yr")
# print(ob.courseName)
print(ob._courseYear)
print(ob._Course__courseDuration)
