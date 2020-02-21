class Student:
    # property
    roll = ""
    gpa = ""

    def __init__(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll : {self.roll}, GPA : {self.gpa}")


rahim = Student(101, 3.64)
rahim.display()

kaim = Student(103, 4.56)
kaim.display()
