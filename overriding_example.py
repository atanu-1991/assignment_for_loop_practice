class Squares:
    def __init__(self,length):
        self.length = length

    def area(self):
        print("Area=",self.length * self.length)


class Rectangles(Squares):
    def __init__(self,width,length):
        super(Rectangles, self).__init__(length)
        self.width = width

    def area(self):
        print("Area=",self.length * self.width)


sqr = Squares(4)
sqr.area()
rec = Rectangles(5,4)
rec.area()