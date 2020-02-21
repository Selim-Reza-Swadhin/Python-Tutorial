class Shape:
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    def area(self):
        print("I am area method of shape class")


class Triangle(Shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("I am area method of triangle class")
        print("Area of Triangle : ", area)


class Rectangle(Shape):
    def area(self):
        area = self.dim1 * self.dim2
        print("I am area method of rectangle class")
        print("Area of Rectangle : ", area)


shape = Shape(10, 20)
shape.area()

tri = Triangle(10, 20)
tri.area()

rect = Rectangle(10, 20)
rect.area()
