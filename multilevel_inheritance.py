class iNeuron:
    num_of_course = 12


class DataScience(iNeuron):
    course_type = "Data-Science"


class AI(DataScience):
    def __init__(self):
        self.company = "iNeuron"
        print("The company {0} offers total {1} different types of courses.Most trending course is {2}".format(
            self.company, self.num_of_course, self.course_type))


ai = AI()