# xxargs function


def sudent(id, name):
    print(id, name)


sudent(101, "Selim")

print("xargs dictionary function")


def student(**details):
    print(details)
    print(details["name"])
    print(details["id"])


student(id=101, name="Selim")
student(id=102, name="Reza", gpa=3.50)
student(id=103, name="Swadhin", gpa=3.50, cllass="One")
