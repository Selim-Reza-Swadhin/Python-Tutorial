class Student:
    # property
    roll = ""
    gpa = ""

    def set_value(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll : {self.roll}, GPA : {self.gpa}")


rahim = Student()
rahim.set_value(101, 3.55)
rahim.display()

kaim = Student()
kaim.set_value(102, 3.65)
kaim.display()
