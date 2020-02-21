class Student:
    # property
    roll = ""
    gpa = ""

    def display(self):
        print(f"Roll : {self.roll}, GPA : {self.gpa}")


rahim = Student()  # object
print("Check object = ", isinstance(rahim, Student))  # check object
rahim.roll = 101
rahim.gpa = 3.75
rahim.display()

kaim = Student()  # object
print("Check object = ", isinstance(kaim, Student))  # check object
kaim.roll = 102
kaim.gpa = 3.00
kaim.display()
