print("Name function")


def calculate(a, b):
    return a * a + 2 * a * b + b * b


print(calculate(2, 3))

print("Lambda function")
print("lambda parameter : expression")

lamda = lambda a, b: a * a + 2 * a * b + b * b
result = (lamda)(2, 3)
print(result)

print((lambda a, b: a * a + 2 * a * b + b * b)(2, 3))

print("Cube")


def cube(x):
    return x * x * x


print("Cube is ", cube(2))

print((lambda x: x * x * x)(2))
