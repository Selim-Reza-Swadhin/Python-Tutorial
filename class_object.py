class Student:
    # property
    roll = ""
    gpa = ""


rahim = Student()  # object
print("Check object = ", isinstance(rahim, Student))  # check object
rahim.roll = 101
rahim.gpa = 3.75

print(f"Roll : {rahim.roll}, GPA : {rahim.gpa}")  # f->formatting

karim = Student()  # object
print("Check object = ", isinstance(karim, Student))  # check object
karim.roll = 102
karim.gpa = 3.00

print(f"Roll : {rahim.roll}, GPA : {rahim.gpa}")  # f->formatting
