# xargs function
def sudent(id, name):
    print(id, name)


sudent(101, "Selim")

print("xargs tuple function")


def student(*details):
    print(details)
    # print(details[0])
    # print(details[1])


student(101, "Selim")
student(101, "Selim", 3.50)
student(101, "Selim", 3.50, "One")


def add(*numbers):
    print(numbers)


add(10, 20)
add(10, 20, 30)
add(10, 20, 30, 40)


def addd(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)


addd(10, 20)
addd(10, 20, 30)
addd(10, 20, 30, 40)
